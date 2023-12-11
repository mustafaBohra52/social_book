from django.shortcuts import render, redirect
from django.http import HttpResponse
from form.models import registerForm


def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password=request.POST.get('password')
        confirmpass=request.POST.get('confirm-password')
        
        if password==confirmpass:
            register = registerForm(username=username,email=email,password=password)
            register.save()
        else:
            return HttpResponse("password is not same")
        
    return HttpResponse("done")

def reg(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")