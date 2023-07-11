from django.contrib import admin

from Administration.models import User,Salle,Professeur,Filiere,Matiere,UE,Semestre,Emploi, Etudiant
# Register your models here.
admin.site.register(User)
admin.site.register(Professeur)
admin.site.register(Matiere)
admin.site.register(Salle)
admin.site.register(Filiere)
admin.site.register(UE)
admin.site.register(Semestre)
admin.site.register(Emploi)
admin.site.register(Etudiant)

