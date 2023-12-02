"""
URL configuration for ProjetDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from Livre.views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('livre/', home),
    path('livre/', home, name='livre'),
    path('create', create, name='create'),
    path('store',  store, name='store'),
    path('upload', uploade, name='upload'),
    path('delete', delete, name='delete'),
    path('download', download_file, name='download_file'),
   # path('search', csrf_exempt(views.search_book), name='searchbook')
    path('search', searchajax, name='searchbook'),
    path('searchcat', csrf_exempt(searchcategorie), name='searchcat'),
    path('apercu/<int:cat_id>/', apercu, name='apercu'),
    path('editcategorie/<int:cat_id>/', editcat, name='editcategorie'),
    path('categorie', categorie, name='categorie'),
    path('catestore', catestore, name='catestore'),
    path('catedelete/<int:cat_id>/', deletecat, name='deletecat'),
    path('telecharger/<int:livre_id>/', telecharger_pdf, name='telecharger'),
    path('afficher_pdf/<int:livre_id>/', afficher_pdf, name='afficher_pdf'),
    path('view_detail/<int:livre_id>/', view_detail, name='afficher_detail'),
    path('creer_comment/<int:livre_id>/', creer_commentaire, name='add_comment'),
    #path('compteur/<int:livre_id>/', store_telecharge, name='compter_telecharge'),
    path('test', test, name='test'),
    path('creer_commande/<int:livre_id>/', commander, name='add_commande'),
    #path('apercubycat/<Char:cat_intitule>/', apercu_by_categorie, name='apercu_cat'),
    path('commandspecial', createspecialCommand, name='specialcommand'),
    path('newsletter', new_letter, name='newletter'),
]
