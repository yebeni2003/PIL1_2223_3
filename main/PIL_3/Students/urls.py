from django.urls import path 
from . import views 
urlspatterns= [
    path('home/',views.studentview),
    path('inscription/', views.inscription_etudiant, name='inscription'),

]

