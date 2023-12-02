from django import forms
from django.forms import ModelForm, TextInput, FileInput, NumberInput
from django.contrib.auth.models import User
from Livre.models import Livre, Categorie
from django.contrib.auth.forms import UserCreationForm
from Users.models import UserCustomize


"""class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prenom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')


    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
"""

class UserRegistrationForm(UserCreationForm):
    Prenom= forms.CharField(label='Prenom')
    Nom= forms.CharField(label='Nom')

    class Meta(UserCreationForm):
        model = UserCustomize
        fields = UserCreationForm.Meta.fields +( 'Prenom', 'Nom'  )


class LivreForm(ModelForm):
   """ titre = forms.CharField(label ='titre')
    auteur = forms.CharField(label ='auteur')
    description = forms.CharField(label ='description')
    couverture = forms.ImageField(label = 'couverture')
    pdf = forms.FileField(label = 'pdf')"""
   class Meta:
        model = Livre
        fields = ('titre', 'auteur', 'description', 'couverture', 'pdf', 'categorie','prix')
        widget = {
                'titre' : TextInput(attrs ={'class':  'form-control'}),
                'auteur' : TextInput(attrs ={'class':  'form-control'}),
                'description' : TextInput(attrs ={'class':  'form-control', 'rows':'4', 'cols': '40'}) ,
                'couverture' : FileInput(attrs ={'class':  'form-control'}),
                'pdf' : FileInput(attrs ={'class':  'form-control'}),
                'categorie' : NumberInput(attrs ={'class':  'form-control,'}),
        
        }
    

class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ('intitule',)
        widget = {
                'intitule' : TextInput(attrs={'class': 'form-control'})
        }