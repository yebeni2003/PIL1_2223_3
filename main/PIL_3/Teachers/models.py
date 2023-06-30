from django.db import models
from django.contrib.auth.models import Teachers


# Create your models here.

class Teachers(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    # Autres champs


class TeachersConnexion(models.Model):
    Teachers = models.OneToOneField(Etudiant, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField
