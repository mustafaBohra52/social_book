from django.db import models
from django import forms

# Create your models here.
class registerForm(models.Model):
    domain=models.CharField(max_length=10,default='select')
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password=models.CharField(max_length=15)
    visibility = models.BooleanField(default=False)
    
class UploadFiles(models.Model):
    title=models.CharField(max_length=50,default="title")
    authorName = models.CharField(max_length=20,default="**")
    desc = models.CharField(max_length=200,null=True)
    files = models.FileField(upload_to='uploads/')
    
class fors(forms.Form):
    file = forms.FileField()
    
  
  

    

