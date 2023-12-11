from django.db import models

# Create your models here.
class registerForm(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password=models.CharField(max_length=15)
    

