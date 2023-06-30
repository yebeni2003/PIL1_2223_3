from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_administration=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    
    
    
    
