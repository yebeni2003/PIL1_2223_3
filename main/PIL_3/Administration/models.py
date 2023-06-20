from django.db import models
# Create your models here.
class Administrator(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField( max_length=100) 
