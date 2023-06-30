from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site 
from .token import generatorToken
from Administration.models import User
from PIL_3 import settings

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.core.mail import send_mail,EmailMessage


# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
       username = request.POST.get('username', '')
       email = request.POST.get('email', '')
       firstname = request.POST.get('firstname', '')
       lastname = request.POST.get('lastname', '')
       password = request.POST.get('password', '')
       password1 = request.POST.get('password1', '')
       if User.objects.filter(username=username):
           messages.error(request,"Ce nom a été déjà pris ")
           return redirect('register')
       
       if User.objects.filter(email=email):
           messages.error(request,"cet email a déjà un compte")
           return redirect('register')
       
       if not username.isalnum():
           messages.error(request,'Le nom doit etre alphanumérique')
           return redirect('register')
       
       if password !=password1:
           messages.error(request,'Les deux mots de passe ne correspondent pas')
           return redirect('register')
           
       mon_utilisateur=User.objects.create_user(username,email,password,is_student=True)
       mon_utilisateur.first_name=firstname
       mon_utilisateur.last_name=lastname
       mon_utilisateur.is_active = False
       mon_utilisateur.save()
       messages.success(request,'Votre compte a été créé avec succès')
       # envoi d'email de bienvenue
       
       
       subject ="Bienvenue sur la plateforme de gestion des emplois du temps de votre institut"
       message= "Bienvenue"+ mon_utilisateur.first_name +" "+mon_utilisateur.last_name+"\n"+"Nous sommes heureux de vous compter parmi nous\n\n\n  merci\n\nTeam3"
       from_email=settings.EMAIL_HOST_USER
       to_list = [mon_utilisateur.email]
       send_mail(subject,message,from_email,to_list,fail_silently=False)
       #email de confirmation
       current_site = get_current_site(request) 
       email_subject = "Confirmation de l'adresse email sur TimeTableForSchool"
       messageConfirm = render_to_string("emailconfirm.html",{
           "name":mon_utilisateur.first_name,
           "domain":current_site.domain,
           "uid":urlsafe_base64_encode(force_bytes(mon_utilisateur.pk)),
           "token":generatorToken.make_token(mon_utilisateur)
           
       })
       email=EmailMessage(
           email_subject,
           messageConfirm,
           settings.EMAIL_HOST_USER,
           [mon_utilisateur.email]
       )
       email.fail_silently = False
       email.send()
       
       return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
       username=request.POST['username']
       password=request.POST['password']
       user=authenticate(username=username,password=password)
       my_user= User.objects.get(username=username)
       if user is not None:
           auth_login(request,user)
           firstname=user.first_name
           return render(request,'index.html',{"firstname":firstname})
       elif my_user.is_active==False:
           messages.error(request,"Vous n'avez pas confirmé votre email.Faites-le avant de vous connecter")
       else:
           messages.error(request,'Mauvaise Authentification ')
           return redirect('login')
    return render(request,'login.html')


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
    
