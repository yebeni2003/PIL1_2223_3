from django.urls import path 
from . import views 
urlpatterns= [
    path('inscription/', views.inscription_etudiant, name='inscription'),
    path('login/success/<str:nom>/<str:prenom>/', views.page_succes, name='page_succes'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login')
]

