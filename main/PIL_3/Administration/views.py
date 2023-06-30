from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .form import UserForm


# Create your views here.
def home(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_student:
                return redirect('student')
            
            elif user.is_administration:
                return redirect('administration')
            else:
                return redirect('student')
        else:
            error= 'password ou username incorrect'
            
        return render(request,'loginall.html',{'error':error})
    
def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'registerall.html',{'form':form})


    
def administration(request):
    return render(request,'administration.html')