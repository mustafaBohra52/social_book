from django.contrib import admin
from form.models import registerForm,UploadFiles

class registerAdmin(admin.ModelAdmin):
    list_display=('domain','username','email','password','visibility')
    
   
class uploadfileAdmin(admin.ModelAdmin):
    list_display=('files',)
    

admin.site.register(registerForm,registerAdmin)
admin.site.register(UploadFiles,uploadfileAdmin)
