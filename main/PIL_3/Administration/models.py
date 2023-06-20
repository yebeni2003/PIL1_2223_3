from django.db import models

# Create your models here.
class Administrator(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField( primary_key=True)
    password = models.CharField( max_length=100) 
#La table pour les cours
class Cours(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    nom = models.CharField(max_length=200)
    masse_horaire = models.IntegerField()
    nom_professeur = models.CharField(max_length=200)
    prenom_professeur = models.CharField(max_length=400)
    salle = models.CharField(max_length=100)
#La table pour les emplois du temps
    
class Emploi(models.Model):
    jours = models.CharField(max_length=8)
    cours = Cours
    duree_heure = models.IntegerField()
#Cette partie concerne la connexion de l'administrateur
class AdministratorConnexion(models.Model):
    administrateur = models.OneToOneField(Adminsitrator, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
