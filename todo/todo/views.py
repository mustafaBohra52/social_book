from django.shortcuts import render,redirect
from todoApp.models import Todo1
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
 


def home(request):
    return render(request,"todohome.html")
@csrf_exempt
def storedata(request):
    title=request.POST.get('title')
    desc = request.POST.get('description')
    
    store = Todo1(title=title,desc=desc)
    store.save()
    
    return HttpResponse('saved')

def readData(request):
    read = Todo1.objects.all()
    return render(request,"readtodo.html",{"read":read})

def dl(request):
    return render(request,"delete.html")

@csrf_exempt
def deletedata(request):
    title=request.POST.get('title')
    
    store = Todo1.objects.get(title=title)
    store.delete()
    
    return HttpResponse('deleted')