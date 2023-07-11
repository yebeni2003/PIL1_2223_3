from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site 
from .token import generatorToken
from Administration.models import User,Emploi,Etudiant
from PIL_3 import settings
from django.urls import reverse

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.core.mail import send_mail,EmailMessage


# Create your views here.
def home(request):
    return render(request,'my_dashboard.html')

from django.contrib.auth.tokens import default_token_generator

def register(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        matricule = request.POST.get("matricule", "")
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        password = request.POST.get('password', '')
        password1 = request.POST.get('password1', '')

        if User.objects.filter(username=username):
            messages.error(request, "Ce nom a déjà été pris")
            return redirect('register')

        if User.objects.filter(email=email):
            messages.error(request, "Cet email est déjà associé à un compte")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, 'Le nom d\'utilisateur doit être alphanumérique')
            return redirect('register')

        if password != password1:
            messages.error(request, 'Les deux mots de passe ne correspondent pas')
            return redirect('register')

        etudiant = Etudiant.objects.filter(matricule_Etu=matricule, nom_Etu=lastname, prenom_Etu=firstname,
                                           email_Etu=email).first()

        if not etudiant:
            messages.error(request, "Le matricule entré n'est pas valide")
            return redirect('register')

        user = User.objects.create(username=username, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.is_active = False
        user.save()

        etudiant.user = user
        etudiant.save()

        # Envoi d'email de bienvenue
        subject = "Bienvenue sur la plateforme de gestion des emplois du temps de votre institut"
        message = "Bienvenue " + user.get_full_name() + "\n" + "Nous sommes heureux de vous compter parmi nous\n\n\n  Merci\n\nTeam3"
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)

        # Email de confirmation
        current_site = get_current_site(request)
        email_subject = "Confirmation de l'adresse email sur TimeTableForSchool"
        message_confirm = render_to_string("emailconfirm.html", {
            "name": user.first_name,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": default_token_generator.make_token(user)
        })
        email = EmailMessage(
            email_subject,
            message_confirm,
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        email.fail_silently = False
        email.send()

        messages.success(request, 'Votre compte a été créé avec succès. Allez confirmer votre email avant de vous connecter')
        return redirect('login')

    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            firstname = user.first_name
            return redirect(reverse('student_schedule'))
        elif user is None:
            messages.error(request, 'Mauvaise Authentification')
        else:
            try:
                my_user = User.objects.get(username=username)
                if not my_user.is_active:
                    messages.error(request, "Vous n'avez pas confirmé votre email. Faites-le avant de vous connecter")
            except User.DoesNotExist:
                messages.error(request, 'Mauvaise Authentification')
            
            return redirect('login')
    
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    messages.success(request,'Vous avez été déconnecté')
    return redirect('home')

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user= User.objects.get(pk=uid)
        
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
        
    if user is not None and generatorToken.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,'Votre compte a bien été activé. Félicitations.Vous pouvez vous connecter maintenant')
        return redirect('login')
    else:
        messages.error(request,'Activation échouée.Réessayez ')
        return redirect('home')
    
def student(request):
    return render(request,'students.html')
    
def etre(request):
      # Rediriger vers la page de profil
    courses = Emploi.objects.all().order_by('semaine')
    grouped_courses = []
    for semaine, group in groupby(courses, key=lambda course: course.semaine):
        grouped_courses.append(list(group))
        # empty_cell = "&nbsp;"
    context = {
        'courses': courses,
        'grouped_courses': grouped_courses
        # 'empty_cell': empty_cell
    }
    return render(request, 'etre.html', context)
