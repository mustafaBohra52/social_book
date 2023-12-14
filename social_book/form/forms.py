from django import forms
from form.models import registerForm

class RegisterForm(forms.ModelForm):
    class Meta:
        model = registerForm
        fields = ['domain','username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
