from django import forms
from .models import Etudiant

class InscriptionEtudiantForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    numero_matricule = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_numero_matricule(self):
        numero_matricule = self.cleaned_data['numero_matricule']
        # Vérifier si le numéro matricule existe dans la base de données
        if not Etudiant.objects.filter(numero_matricule=numero_matricule).exists():
            raise forms.ValidationError("Le numéro matricule n'est pas valide.")
        return numero_matricule
