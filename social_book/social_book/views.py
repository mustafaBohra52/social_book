from django.shortcuts import render, redirect
from django.http import HttpResponse
from form.models import registerForm , UploadFiles
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from form.forms import RegisterForm
from form.forms import Upload
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from sqlalchemy import create_engine
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os

engine = create_engine('postgresql://mustafabohra:mustafabohra@localhost:5432/mydatabase',echo=True)


    
def reg(request):
    return render(request,"register.html")

def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            print("log page")
            print(request.user.username)
            request.session['username'] = user.username
            login(request,user)
            
            return redirect('dashboard')
        else:
            a="invalid credential"
            return HttpResponse("Invalid Login Details")
    return render(request,"login.html")



            
       
    
def userpage(request):
    users = registerForm.objects.all()
    data={"users":users}
    return render(request,"userPage.html",data)



@login_required
def dashboard(request):
    print("dashboard")

    return render(request,"Dashboard.html")
    
# @login_required
def authorpage(request):
    print("-" * 30)
    print("username : -")
    print(request.user.username)
    print("-" * 30)
    author = registerForm.objects.filter(username=request.user.username,domain="Author",visibility=True)
    
    data={"domain":author}
    
    print(author)
    return render(request,"authorspage.html",data)
        
   

def sellerpage(request):
    print(request.user.username)
    seller = registerForm.objects.filter(username=request.user.username,domain="Seller",visibility=True)
    print(seller)
    data = {"domain":seller}
    
    return render(request,'sellerpage.html',data)
    

@csrf_exempt
def uploadFile(request):
    if request.method=="POST":
        author=request.POST.get("author")
        title=request.POST.get('title')
        desc = request.POST.get('desc')
        media ='D:/Markytics/social_book/social_book/media/uploads'
        
        file = os.path.join(media,request.POST.get('file'))
        
        
        store = UploadFiles(files=file,authorName=author,title=title,desc=desc)
        store.save()
        
    return render(request,"uploadFiles.html")
    

@csrf_exempt
def auth(request):
    username=request.POST.get('username')
    email = request.POST.get('email')
    password=request.POST.get('password')
    domain=request.POST.get('domain')
    confirm = request.POST.get('confirm-password')

    visibility = request.POST.get('public_visibility')
   
    
    if visibility=="on":
        print(visibility)
        visibility=True
    else:
        print(visibility)
        visibility=False
    
    if password==confirm:
        user = User.objects.create_user(username=username,
                                                password=password,
                                                email=email)
        
        user.save()
        store = registerForm(username=username,email=email,domain=domain,visibility=visibility)
        store.save()
        return redirect('login')
        # return render(request,"register.html",{"p":password,"c":confirm})
    else:
        messages.warning(request,'password is not same')
        return redirect('/')
        return HttpResponse("password is not same")
        
    #log(username,password)
        
    

def logoutss(request):
    logout(request)
    return redirect("login")

def show_uploads(request):
    file = UploadFiles.objects.all()
    data={"file":file}
    return render(request,'showUploadFile.html',data)

def myBook(request):
    # if registerForm.objects.filter(username=request.user.username,domain="Author",visibility=True) or registerForm.objects.filter(username=request.user.username,domain="Seller",visibility=True):
    file = UploadFiles.objects.all()
    data={"file":file}
    # else:
        # return HttpResponse("no file uploaded")
    return render(request,"myBook.html",data)
    
    
# import psycopg2
# from psycopg2 import sql

# # Replace these values with your actual database credentials
# db_config = {
#     'host': 'localhost',
#     'database': 'todo',
#     'user': 'mustafabohra',
#     'password': 'mustafabohra',
#     'port': '5432',  # Usually 5432 for PostgreSQL
# }

# def fetch_data_from_database():
#     try:
#         connection = psycopg2.connect(**db_config)

#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM form_registerform")
        
#         result = cursor.fetchall()
#         print({'result':result})
#         return result
        

#     except psycopg2.Error as e:
#         print(f"Error: {e}")

#     finally:
#         # Close the cursor and connection
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Example SQL query


# result=fetch_data_from_database()

# def create_dbFrame(sql_queary):
#     coloumn = ['id','username','email','password','domain','visibility']
#     df = pd.DataFrame(sql_queary,columns=coloumn)
#     print(df)
    
# create_dbFrame(result)
    





