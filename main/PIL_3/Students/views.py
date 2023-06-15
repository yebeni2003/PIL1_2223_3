from django.shortcuts import render

# Create your views here.
def studentview(request):
    return render(request,'home.html')