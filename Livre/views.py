from tkinter import Canvas
from wsgiref.types import FileWrapper
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.html import format_html
from django.urls import reverse_lazy
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from Livre.models import *
import os
import mimetypes
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, ListView
from django.http import FileResponse, HttpResponseRedirect, JsonResponse, HttpResponse, StreamingHttpResponse
from django.template.loader import render_to_string
from ProjetDjango.forms import LivreForm, CategorieForm
import json
from django.core.paginator import Paginator
import datetime
import csv
import xlwt
from django.template.loader import render_to_string
#from WeasyPrint import HTML
import tempfile




# Create your views here.
@login_required()
def home(request):
    list_livre=Livre.objects.all().order_by('publication_date')
    cat = Categorie.objects.all()
    nombre_notifications = Notification.objects.filter(is_read= False, recipient=request.user).count()
    notifications = Notification.objects.filter(recipient = request.user)
    paginator = Paginator( list_livre, 2)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    if request.method == "GET":
        name = request.GET.get('rechercher')
        if name is not None:
           list_livre=Livre.objects.filter(titre__icontains=name)
    context = {'list_livre':list_livre, 'cat': cat, 'page_obj':page_obj, 'notification_nombre': nombre_notifications,'notifications': notifications }
    return render(request,'index.html', context)
   # return render(request, template_name='biblioP.html',context={'list_Livre':list_Livre})

def create(request):
    return render(request,'create.html')

def store(request):
    if request.method =='POST':
        titre = request.POST['titre']
        auteur = request.POST['auteur']
        description = request.POST['description']
        couverture = request.FILES['couverture']
        pdf = request.FILES['pdf']
        prix = request.POST['prix']
        book = Livre(titre=titre, auteur=auteur, description=description, couverture = couverture,  pdf = pdf, prix = prix)
        book.save()
        messages.success(request, 'Livre ajoute avec succes')
        return redirect('livre')
    else:
        messages.error(request, 'Livre non enregistre')
        return redirect('livre')

def uploade(request):
    if request.method =='POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('livre')
        else:
            messages.error(request, 'Erreur, Information incorrectes !')
            return render(request,'uploade.html', {'form':form})
    else:
     form = LivreForm()
    return render(request,'uploade.html', {'form':form})


def delete(Livre_id):
    Livre = Livre.objects.get(pk=Livre_id).delete()
    return redirect(home)

@login_required()
def apercu(request,cat_id):
    categorie = get_object_or_404 ( Categorie, pk=cat_id)
    livre= Livre.objects.filter(categorie = cat_id)
    context={'livre':livre, 'categorie':categorie}
    return render(request,'apercu.html', context)

@login_required()
def apercu_by_categorie(request,cat_intitule):
    categorie = get_object_or_404 ( Categorie, intitule=cat_intitule)
    livre= Livre.objects.filter(categorie = categorie)
    context={'livre':livre, 'categorie':categorie}
    return render(request,'apercu.html', context)


@login_required()
def categorie(request):
    cat = Categorie.objects.all()
    paginator = Paginator( cat, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    nombre_notifications = Notification.objects.filter(is_read= False, recipient=request.user).count()
    notifications = Notification.objects.filter(recipient = request.user)
    context = { 'page_obj':page_obj, 'cat':cat,'notification_nombre': nombre_notifications,'notifications': notifications,}
    return render(request, 'categorie.html',context)

@login_required()
def catestore(request):
    if request.method =='POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operation Reussi !')
            return redirect(categorie)
        else:
            messages.error(request, 'Erreur, Information invalide')
            return redirect(categorie)
    else:
      form = CategorieForm()
    #messages.warning(request, 'attention')
    #messages.info(request, 'Infon')
    
    return render(request,'categoriecreate.html', {'form':form})

@login_required()
def editcat(request, cat_id):
    if request.method =='POST':
        cat = Categorie.objects.get(pk=cat_id)
        form = CategorieForm(request.POST, instance = cat)
        if form.is_valid():
            form.save()
            messages.success(request,' Modifications effectue avec succés ! ')
            return redirect(categorie)
    else:
       cat = Categorie.objects.get(pk=cat_id)
       form = CategorieForm( instance = cat)
    return render(request,'updatecat.html', {'form':form})
@login_required()
def deletecat(request, cat_id):
    Categorie.objects.get(pk=cat_id).delete()
    #messages =" Categorie suprimée avec succè !"
    return redirect(categorie)
@login_required()
def download_file(request, livre_id):
    filename=get_object_or_404(Livre, pk=livre_id)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath=filename.pdf.path
    path = open(filepath, 'rb')
    mime_type= mimetypes.guess_type(filepath)
    return redirect(home)


@login_required()
def telecharger_pdf(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    chemin_pdf = livre.pdf.path
    now = datetime.datetime.now()
    date_format = now.strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"rapport_{date_format}.pdf"
    response = FileResponse(open(chemin_pdf, 'rb'), as_attachment=True)
    response['Content-Type']='application/pdf'
    response['Content-Disposition'] = 'Attachment; filename = %s'% filename
    #return redirect('compter_telecharge', livre_id=livre_id)

    telechargeur = request.user
    compteur = compteur_de_telechargement(livre = livre, telechargeur = telechargeur)
    compteur.save()

    """notification_message="a telechargé le livre"""
    notification_type='telechargement'
    notification_message = 'a telechargeé ce livre, titre: '+livre.titre + ', auteur : '+livre.auteur
    notification = Notification(recipient = telechargeur, message=notification_message, type=notification_type)
    notification.save()

    return response



"""def telecharger_pdf(request, livre_id):
    now = datetime.datetime.now()
    date_format = now.strftime("%Y-%m-%d-%H-%M-%S")
    nom_fichier_pdf = f"rapport_{date_format}.pdf"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath= BASE_DIR + '/Files/'+ nom_fichier_pdf
    filename= os.path.basename(filepath)
    chunk_size=8192
    response = StreamingHttpResponse(FileWrapper(open(filepath,'rb'),chunk_size), content_type =mimetypes.guess_type(filepath)[0])
    response['Content-Lengtt'] = os.path.getsize(filepath)
    response['Content-Disposition'] = "Attachment; filename=%s"% filename
    return response

def telecharger_pdf(request, livre_id):
    #now = datetime.datetime.now()
    #date_format = now.strftime("%Y-%m-%d-%H-%M-%S")
    #nom_fichier_pdf = f"rapport_{date_format}.pdf"
    #chemin_absolu_pdf = os.path.join("chemin/vers/votre/dossier/de/pdf", nom_fichier_pdf)
    
    # Récupérez le modèle PDF en fonction de l'ID ou tout autre critère.
    livre = get_object_or_404(Livre, id=livre_id)
    # Ouvrez le fichier PDF en mode binaire.
    with open(livre.pdf.path, 'rb') as pdf_file:
        response = FileResponse(pdf_file, content_type='application/pdf')
        # Spécifiez le nom du fichier lors du téléchargement.
        response['Content-Disposition'] = f'attachment; filename="{nom_fichier_pdf}"'
        return response
"""
@login_required()
def afficher_pdf(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    return render(request, 'pdf_viewer.html', {'livre': livre})

@login_required()
def view_detail(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    comments = Commentaire.objects.filter(livre=livre)
    return render(request, 'view_detail.html', {'livre': livre, 'comments':comments})


@login_required()
def search_book(request):
    query=request.GET.get('query')
    if not query:
        Livre = Livre.objects.all()
    else:
        Livre = Livre.objects.filter(titre__icontains = query)
        if not Livre.exists():
            messages ='Aucun Livre trouvé'
    return render(request,'home.html', content_type={'Livre':Livre, 'message':messages})

@login_required()
def searchajax(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        income = Livre.objects.filter(titre__istartswith =search_str) | Livre.objects.filter(auteur__istartswith=search_str) | Livre.objects.filter(description__icontain = search_str)
        data = income.values()
        return JsonResponse(list(data), safe=False)
@login_required()    
def searchcategorie(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        cat = Categorie.objects.filter(intitule__istartswith =search_str) | Categorie.objects.filter(id__istartswith=search_str)
        data = cat.values()
        return JsonResponse(list(data), safe=False)




def export_pdf(resuest):
    response= HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='inline'; 'attachment; filename=livre'+\
    str(datetime.datetime.now())+'.pdf'
    response['content-Transfer-Encoding'] = 'binary'
    html_string = render_to_string('livre/pdf-output.html', {'livre':[],'total':0})
    html = HTML(string=html_string)
    result = html.write_pdf()
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name,'rb')
        response.write(output.read())      
    return response

def export_csv(resuest):
    response= HttpResponse(content_type='text/csv')
    response['Content-Disposition']='inline'; 'attachment; filename=livre'+\
    str(datetime.datetime.now())+'.csv'  
    writer = csv.writer(response)
    writer.writerow(['montant',' description', 'categorie'])
    livre= Livre.objects.filter(titre__icontain='charlotte')
    for livre in livre:
        writer.writerow([livre.auteur, livre.titre, livre.description])
    return response


def export_excel(resuest):
    response= HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='inline'; 'attachment; filename=livre'+\
    str(datetime.datetime.now())+'.xls'
    wb = xlwt.workboook(encodinf= 'utf-8')
    ws = wb.add_sheet('livre')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['titre', 'auteur', 'description']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        rows = Livre.objects.filter(auteur__icontain= 'charloote').values.list('titre', 'auteur', 'description')
    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    ws.save()
    return response


def livre_categorie_summary(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date-datetime.timedelta(day=30*6)
    livre = Livre.objects.filter(auteur__icontain= 'charlotte',date__gte= six_months_ago,date_lte= todays_date)
    finalrep = {}

    def get_category(livre):
        return livre
    category_list = list(set(map(get_category, livre)))

    def get_livre_category_amount(category):
        amount = 0
        filtered_by_category = Livre.objects.filter(categorie = category)
        for item in filtered_by_category: 
            amount+=item.amount
        return amount

    for x in livre:
        for y in category_list:
             finalrep[y] = get_livre_category_amount 
    return JsonResponse({' livre_data':finalrep}, safe = False)

    def stat_views(request):
        return render(request)
    


def generer_pdf():
    # Générer le nom du fichier PDF basé sur l'heure et la date actuelles
    maintenant = datetime.datetime.now()
    nom_fichier_pdf = maintenant.strftime("%Y-%m-%d_%H-%M-%S") + ".pdf"

    # Générer le contenu du fichier PDF (dans cet exemple, un PDF vide)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{nom_fichier_pdf}"'

    c = Canvas.Canvas(response, pagesize=letter)
    c.drawString(100, 750, "Bonjour, ceci est un PDF généré à partir de Django.")
    c.showPage()
    c.save()

    return response


"""def store_telecharge(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    telechargeur = request.user
    livre = compteur_de_telechargement(livre = livre, telechargeur = telechargeur)
    livre.save()
    messages = "Téléchargement reussit!"
    return redirect('livre')
    """
@login_required()
def create_notification(request, recipient, message, type):
    notification = Notification(recipient=recipient, type=type, message=message)
    notification.save()


@login_required()
def view_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(recipient=user, is_read=False)
    return render(request, 'notifications.html', {'notifications': notifications})


@login_required()
def mark_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.is_read = True
    notification.save()


@login_required
def creer_commentaire(request, livre_id):
    if request.method == 'POST':
        livre = get_object_or_404(Livre, pk=livre_id)
        auteur = request.user
        email = request.POST.get("email")
        nomprenom = request.POST.get("nomprenom")
        contenu = request.POST.get("commentaire")
        comment = Commentaire(livre = livre, auteur = auteur, email = email, nomprenom = nomprenom, contenu = contenu)
        comment.save()
        """ if formulaire.is_valid():
            nouveau_commentaire = formulaire.save(commit=False)
            nouveau_commentaire.livre_id = livre_id  # Associer le commentaire au livre
            nouveau_commentaire.save()
            return redirect('detail_livre', livre_id=livre_id)  # Rediriger vers la page de détail du livre
    """
    #comments = Commentaire.objects.filter(livre = livre)
        notification_type='commentaire'
        notification_message = 'a commenté le livre : titre'+livre.titre + 'auteur = '+livre.auteur
        notification = Notification(recipient=auteur, message=notification_message, type=notification_type)
        notification.save()
    return redirect('livre')# render(request, 'view_detail.html', {'comments': comments})


def test(request):
    return render(request, 'test.html')


@login_required()
def commander(request, livre_id):
    if request.method =='POST':
        livre = get_object_or_404(Livre, pk=livre_id)
        auteur = request.user
        commande = Commande(livre = livre, utilisateur = auteur)
        commande.save()
        messages.success(request, 'Félicitation! Votre commande a été traitée avec succès.')

        #Notification
        notification_type='commande'
        notification_message = 'a commande le livre : titre'+livre.titre + 'auteur = '+livre.auteur
        notification = Notification(recipient=auteur, message=notification_message, type=notification_type)
        notification.save()
    return redirect('livre')

@login_required()
def createspecialCommand(request):
    if request.method == 'POST':
        if 'couverture' in request.FILES:
              couverture = request.FILES['couverture']
        else:
             couverture = ''
        livre_titre =  request.POST['titre']
        livre_auteur =  request.POST['auteur']
        nom_prenom = request.POST['nomprenom']
        date =request.POST['date']
        couverture = couverture
        auteur = request.user
        if request.POST['date']:
            commandespec = Commande_special.objects.create(nom_prenom =nom_prenom, livre_titre = livre_titre,  utilisateur = auteur, livre_auteur = livre_auteur, couverture = couverture, livre_date_pub=date)
            commandespec.save()
        else:
             commandespec = Commande_special.objects.create(nom_prenom =nom_prenom, livre_titre = livre_titre,  utilisateur = auteur, livre_auteur = livre_auteur, couverture = couverture)
             commandespec.save()
        messages.success(request, 'Félicitation! Votre commande a été traitée avec succès.')

        #Notification
        notification_type='commande speciale'
        notification_message = 'a commandé un livre spéciale : titre'+livre_titre + 'auteur = '+livre_auteur
        notification = Notification(recipient=auteur, message=notification_message, type=notification_type)
        notification.save()
        return redirect('livre')



def new_letter(request):
    if request.method == 'POST':
        email = request.POST['email']
        newlet = newsletter(email = email)
        newlet.save()
        messages.success(request,'Felicitation !, vous allez recevoir les nouvelles du site Livre Numeriques Burkina !')
    return redirect('livre')