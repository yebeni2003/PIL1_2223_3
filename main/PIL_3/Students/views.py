from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout


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
           messages.error(request,'Les deux mots de passe ne correspo')
           
           
       mon_utilisateur=User.objects.create_user(username,email,password)
       mon_utilisateur.first_name=firstname
       mon_utilisateur.last_name=lastname
       mon_utilisateur.save()
       messages.success(request,'Votre compte a été créé avec succès')
       return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
       username=request.POST['username']
       password=request.POST['password']
       user=authenticate(username=username,password=password)
       if user is not None:
           auth_login(request,user)
           firstname=user.first_name
           return render(request,'index.html',{"firstname":firstname})
       else:
           messages.error(request,'Mauvaise Authentification ')
           return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth_logout(request)
    messages.success(request,'Vous avez été déconnecté')
    return redirect('home')