from django.contrib import admin
from Livre.models import Livre, Categorie, Notification, Commentaire, compteur_de_telechargement, Commande, Commande_special, newsletter
from Users.models import UserCustomize
# Register your models here.



admin.site.register(compteur_de_telechargement)
admin.site.register(Commentaire)
admin.site.register(Notification)
admin.site.register(Categorie)
admin.site.register(Livre)
admin.site.register(UserCustomize)
admin.site.register(Commande)
admin.site.register(newsletter)
admin.site.register(Commande_special)
""" class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre','auteur', 'description',  'couverture', 'pdf')
 """
