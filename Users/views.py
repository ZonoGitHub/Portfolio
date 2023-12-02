from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model,logout,login,authenticate
from ProjetDjango.forms import UserRegistrationForm, UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from Livre.models import Livre
from django.core.paginator import Paginator

""" import threading
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, djangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site 
 """

# Create your views here.


#if not request.user.is_authenticated:
#      return redirect(f"{settings.LOGIN_URL}?next={request.path}")
#return render(request, "myapp/login_error.html")

#@login_required(login_url="/login")
 # if not request.user.is_authenticated:
       # return render(request,'login.html')
def homme(request):
    #livre = Livre.objects.all()[:3]
    livre1 = Livre.objects.get(pk=1)
    livre2 = Livre.objects.get(pk=2)
    livre3 = Livre.objects.get(pk=3)
   # Paginator = Paginator(livre, 9)
    return render (request,'homme.html', { 'livre1': livre1, 'livre2': livre2, 'livre3': livre3})



""" class emailThread(threading.Thread):
    
    def __init__(self,email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)

 """
def register(request):

    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()     
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user) 
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')                  
            return redirect('home')
    else :
        form = UserRegistrationForm()
    return render(request,'register.html',{'form' : form})

"""def login_users(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('home')
           
    return render(request, 'login.html',{'form': form})"""



"""def logout_users(request):
    logout(request)
    return render(request, 'login.html')"""


"""User = get_user_model()
# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not user.objects.filtter  (username=username).exists():
           if not user.objects.filtter     (email=email).exists():
              if len(password) < 6:
                  message.error(request, 'password         too short'
                 return render(request,         'authentication/register.html',         context)
            user =User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.is_activate = False
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get-current_site(request).domain
            link = reverse('activate', kwargs = {
            'uidb64':uidb64, 'token':token})

            domain=get_current_site(request).domain
            link= reverse('activate', kwargs={'uidb64':uidb64, 'token': token})
            email_body = 'test body'
            email_subject = 'activate your account'
            email = EmailMessage(
            email_subject, email_body, 'noreply@semycolon.com',[email],
            )
            email.send(fail_silently =False)
            message.success(request, 'Account successfully created')
            return render(request, 'authentication/register.html')



        user = User.objects.create_user(username = username,password=password)
        login(request,user)
        return redirect('accueil')
    return render(request, 'compte/signup.html')

def login_users(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username,password=password)
        if user:
            login(request, user)
            return redirect('accueil')
    return render(request, 'compte/login1.html')

def logout_users(request):
    logout(request)
    return render(request, 'compte/login1.html')"""



""" class verificationView(View):
  def get(self, request, uidb64, token):
      return redirect('login') """