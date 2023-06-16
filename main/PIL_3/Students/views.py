
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .forms import InscriptionEtudiantForm

# Create your views here.
def studentview(request):
    return render(request,'home.html')


def inscription_etudiant(request):
    if request.method == 'POST':
        form = InscriptionEtudiantForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            numero_matricule = form.cleaned_data['numero_matricule']
            password = form.cleaned_data['password']

            # Créer un nouvel utilisateur Django
            user = User.objects.create_user(username=username, email=email, password=password)

            # Récupérer l'étudiant correspondant au numéro matricule
            etudiant = Etudiant.objects.get(numero_matricule=numero_matricule)

            # Enregistrer les identifiants de connexion de l'étudiant
            etudiant_connexion = EtudiantConnexion(etudiant=etudiant, username=username, password=password)
            etudiant_connexion.save()

            # Rediriger vers la page de succès d'inscription avec le nom et prénom de l'étudiant
            return redirect('page_succes', nom=etudiant.nom, prenom=etudiant.prenom)
    else:
        form = InscriptionEtudiantForm()
    
    return render(request, 'inscription_etudiant.html', {'form': form})


def page_succes(request, nom, prenom):
    return render(request, 'page_succes.html', {'nom': nom, 'prenom': prenom})

