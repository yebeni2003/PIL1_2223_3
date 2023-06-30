from django.urls import path
from .views import home,administration,register

urlpatterns = [
    path('',home,name='home'),
    path('register2',register,name='register2'),
    path('adminitration',administration,name='administration')
]
