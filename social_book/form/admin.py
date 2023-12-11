from django.contrib import admin
from form.models import registerForm

class registerAdmin(admin.ModelAdmin):
    list_display=('username','email','password')
    
    

# Register your models here.
admin.site.register(registerForm,registerAdmin)