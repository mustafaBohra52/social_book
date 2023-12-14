from django.contrib import admin
from todoApp.models import Todo1

class Admin(admin.ModelAdmin):
    list_display=('title','desc')
    

# Register your models here.
admin.site.register(Todo1,Admin)
