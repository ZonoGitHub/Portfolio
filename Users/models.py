from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class UserCustomize(AbstractUser):
    Prenom = models.CharField()
    Nom = models.CharField()
   # Email = models.EmailField(unique=True)
    #username = None
    #USERNAME_FIELD = 'email'
    def __str__(self):
        return self.Nom + "  / "+self.Prenom +"  / "+self.username
    