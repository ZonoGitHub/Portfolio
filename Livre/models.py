from django.utils.timezone import now
from django.db import models
from email.policy import default
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.



class Categorie(models.Model):
      intitule = models.CharField(max_length=250, null=False, unique=True)
      date = models.DateTimeField(auto_now_add=True)




      def __str__(self):
            return self.intitule
      class meta:
            verbose_name = 'Categorie'
            verbose_name_plural = 'Categorie'


class Livre(models.Model):
      titre = models.CharField(max_length=250, null=False)
      auteur = models.CharField(max_length=250, null=False)
      download_number = models.IntegerField(default=0)
      description = models.TextField(null=True, default='none')
      couverture = models.ImageField(upload_to = 'couverture', null=False)
      pdf=models.FileField(upload_to='pdf', null=False)
      categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
      publication_date = models.DateField(null=True, default='2000-12-31')
      prix = models.BigIntegerField(default=0)

      def __str__(self):
            return self.titre
      class meta:
            verbose_name = 'Livre'
            verbose_name_plural = 'Livre'


class compteur_de_telechargement(models.Model):
      telechargeur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
      date = models.DateTimeField(auto_now_add=True)



      def __str__(self):
            return self.telechargeur
      class meta:
            verbose_name = 'telechargeur'
            verbose_name_plural = 'telechargeur'



class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications', null=True, default='none')
    message = models.TextField()
    type = models.CharField(default='none')
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.type



class Commentaire(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Nom de l'utilisateur qui a posté le commentaire
    contenu = models.TextField()  # Le contenu du commentaire
    nomprenom = models.CharField(null=True)
    email = models.EmailField(max_length=250, null=True)
    date_poste = models.DateTimeField(auto_now_add=True)  # Date et heure de la publication
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)  # Lien vers le livre associé
    is_valide = models.BooleanField(default=False)

    def __str__(self):
        return self.contenu  # Vous pouvez personnaliser cette méthode pour afficher autre chose


class Commande(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    #quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Commande du livre: {self.livre.titre} par {self.utilisateur.username}"
    
class Commande_special(models.Model):
    nom_prenom = models.CharField(max_length=255, blank=True, null=True)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    livre_titre = models.CharField(null=True)
    livre_auteur = models.CharField(null=True)
    livre_date_pub= models.DateField(null=True, default='2000-12-31')
    date_commande = models.DateTimeField(auto_now_add=True)
    couverture = models.ImageField(upload_to = 'couverture_speciale', null=True, blank=True)
    #quantite = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"Commande spéciale d'un livre titre: {self.livre_titre}, auteur :{self.livre_auteur} par {self.utilisateur.username}"
    

class newsletter(models.Model):
     email= models.EmailField(null=False)
     def __str__(self):
          return self.email