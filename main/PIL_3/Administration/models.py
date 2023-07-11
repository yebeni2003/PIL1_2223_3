from django.db import models
from django.contrib.auth.models import AbstractUser
import random
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_administration = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Emploi(models.Model):
  
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    subject = models.ForeignKey('Matiere', on_delete=models.CASCADE)
    classroom = models.ForeignKey('Salle', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Professeur', on_delete=models.CASCADE)
    filiere = models.ForeignKey('Filiere', on_delete=models.CASCADE)
    current_time_used = models.IntegerField(default=0)
    semestre = models.ForeignKey('Semestre',on_delete = models.CASCADE, default = 1)
    week_num = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default= False)

    

    def __str__(self):
        return self.subject.nom_mat

class Filiere(models.Model):
    id_fil = models.IntegerField(primary_key=True)
    nom_fil = models.CharField(max_length=50)
    
    def serialize(self):
        return {
            'id':self.id_fil,
            'nom_fil':self.nom_fil,
        }
    def __str__(self):
        return self.nom_fil

class Matiere(models.Model):
    
    global CODES_COULEURS
    CODES_COULEURS = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF',
                  '#FF4500', '#8A2BE2', '#32CD32', '#FF69B4', '#00CED1', '#FF8C00',
                  '#008B8B', '#9400D3', '#FFD700', '#6A5ACD', '#2E8B57', '#BA55D3',
                  '#FFA500', '#6495ED']
    
    def choice():
       return random.choice(CODES_COULEURS)
    
    id_mat = models.IntegerField(primary_key=True)
    nom_mat = models.CharField(max_length=50)
    horaire_mat = models.IntegerField()
    code_ue = models.ForeignKey('UE', on_delete=models.CASCADE)
    masse_horraire_utilisee = models.IntegerField(default=0)
    bgColor = models.CharField(default= choice(), null=True, blank=True, max_length=100)
    id_filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, null=True)
    def serialize(self):
        return {
            'id': self.id_mat,
            'nom_mat': self.nom_mat,
            'bgColor': self.bgColor,
            'filiere': self.id_filiere.serialize(),
            'masse_horraire_utilisee':self.masse_horraire_utilisee,
            'horaire_mat':self.horaire_mat
        }

    def __str__(self):
        return self.nom_mat

class UE(models.Model):
    code_ue = models.CharField(max_length=10, primary_key=True)
    nom_ue = models.CharField(max_length=100)
    nombre_credit_ue = models.IntegerField()
    type_semestre_ue =  models.ForeignKey('Semestre', on_delete=models.CASCADE)
    id_fil = models.ForeignKey('Filiere',on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.nom_ue

class Salle(models.Model):
    id_sal = models.CharField(max_length=20, primary_key=True)
    desc = models.TextField(null=True)
    nom_sal = models.CharField(max_length=20)
    cap_sal = models.IntegerField()

    

    def serialize(self):
        return {
            'id': self.id_sal,
            'nom_sal': self.nom_sal,
            'cap_sal': self.cap_sal,
            'desc': self.desc,

            
        }


    def __str__(self):
        return self.nom_sal

class Professeur(models.Model):
    id_prof = models.IntegerField(primary_key=True)
    nom_prof = models.CharField(max_length=50)
    prenom_prof = models.CharField(max_length=100)
    sexe_prof = models.CharField(max_length=1)
    contact_prof = models.IntegerField(null=True)
    email_prof = models.EmailField()
    matiere_enseigne = models.ForeignKey('Matiere',on_delete = models.CASCADE,default=1)
    def serialize(self):
        return {
            'id': self.id_prof,
            'nom_prof': self.nom_prof,
            'prenom_prof': self.prenom_prof,
            'email': self.email_prof,
            'matiere':self.matiere_enseigne
        }
    

    def __str__(self):
        return f"{self.prenom_prof} {self.nom_prof}"

class Semestre(models.Model):
    type_semestre = models.IntegerField(primary_key=True)
    

class Etudiant(models.Model):
    matricule_Etu = models.IntegerField(primary_key=True)
    nom_Etu = models.CharField(max_length=50)
    prenom_Etu = models.CharField(max_length=100)
    sexe_Etu = models.CharField(max_length=1)
    date_nais_Etu = models.DateField(null=True)
    contact = models.IntegerField(unique=True)
    email_Etu = models.EmailField(unique=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return f"{self.nom_Etu} {self.prenom_Etu}"
