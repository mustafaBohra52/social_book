from django.db import models

class Todo1(models.Model):
    title=models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    
# Create your models here.
