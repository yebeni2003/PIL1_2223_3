from django.shortcuts import render, redirect
from .models import Etudiant, EtudiantConnexion
from django.contrib.auth.models import User,auth
from django.db import IntegrityError
from .forms import InscriptionEtudiantForm
from django.contrib import messages
# Create your views here.
def studentview(request):
    return render(request, 'home.html')


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

            try:
                # Récupérer l'étudiant correspondant au numéro matricule
                etudiant = Etudiant.objects.get(numero_matricule=numero_matricule)

                # Vérifier si une instance EtudiantConnexion existe déjà pour cet étudiant
                etudiant_connexion = EtudiantConnexion.objects.get(etudiant=etudiant)
                
                # Une instance EtudiantConnexion existe déjà pour cet étudiant
                # Vous pouvez gérer cette situation en affichant un message d'erreur approprié ou en effectuant d'autres actions nécessaires.

            except Etudiant.DoesNotExist:
                # L'étudiant n'existe pas
                # Gérer cette situation en affichant un message d'erreur approprié ou en effectuant d'autres actions nécessaires.
                pass
            
            except EtudiantConnexion.DoesNotExist:
                # Aucune instance EtudiantConnexion existante pour cet étudiant
                # Enregistrer les identifiants de connexion de l'étudiant
                etudiant_connexion = EtudiantConnexion(etudiant=etudiant, username=username, password=password)
                etudiant_connexion.save()
            user = User.objects.create_user(username=username, email=email, password=password)

                # Rediriger vers la page de succès d'inscription avec le nom et prénom de l'étudiant
            return render(request, 'inscription_etudiant.html', {'form': form, 'success': True, 'name': etudiant.nom, 'surname': etudiant.prenom})
                
            

    else:
        form = InscriptionEtudiantForm()
    
    return render(request, 'inscription_etudiant.html', {'form': form})


def page_succes(request, nom, prenom):
    return render(request, 'page_sucess.html', {'nom': nom, 'prenom': prenom})


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                messages.info(request,True)
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('register')
    else:
        return render(request,'register.html')
    
            
              
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password=request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            redirect('login')
    return render(request,'login.html')        

def logout(request):
    auth.logout(request)
    return redirect('/')