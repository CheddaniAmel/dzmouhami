from django.contrib import admin
from .models import specialisation,Langue,Avocat,Client,ProfilAvocat,Blog,RendezVous,Avis


# Register your models here.
admin.site.register(Avocat)
admin.site.register(Client)
admin.site.register(ProfilAvocat)
admin.site.register(Blog)
admin.site.register(RendezVous)
admin.site.register(specialisation)
admin.site.register(Langue)
