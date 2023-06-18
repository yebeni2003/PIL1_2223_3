from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Etudiant(models.Model):
    numero_matricule = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    # Autres champs


class EtudiantConnexion(models.Model):
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    