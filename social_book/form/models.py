from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager

# Create your models here.
class registerForm(models.Model):
    domain=models.CharField(max_length=10,default='select')
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password=models.CharField(max_length=15)
    visibility = models.BooleanField(default=False)
    
class UploadFiles(models.Model):
    files = models.FileField(upload_to='uploads/')
  
  

    

