from django.db import models
# Create your models here.
class Administrator(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField( max_length=100) 

class Emploi(models.Model):
    cours = models.CharField(max_length=200)
    heure = models.CharField(max_length=5)
    duree_heure = models.IntField()
class AdministratorConnexion(models.Model):
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
