from django import forms
from form.models import registerForm,UploadFiles
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    class Meta:
        model = User
        fields = ['domain','username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        


class Upload(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ['files']
