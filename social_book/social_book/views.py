from django.shortcuts import render, redirect
from django.http import HttpResponse
from form.models import registerForm , UploadFiles
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from form.forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from sqlalchemy import create_engine
import pandas as pd
from django.contrib.auth.decorators import login_required

engine = create_engine('postgresql://mustafabohra:mustafabohra@localhost:5432/mydatabase',echo=True)


    

@csrf_exempt

def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password=request.POST.get('password')
        confirmpass=request.POST.get('confirm-password')
        
        if request.POST.get('password')==request.POST.get('confirm-password'):
            register = registerForm(username=username,email=email,password=password)
            register.save()
        else:
            return HttpResponse("password is not same")
        
    return redirect("login")
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username=request.POST.get('username')
    #         email = request.POST.get('email')
    #         password=request.POST.get('password')
    #         domain=request.POST.get('domain')
    #         visibility = request.POST.get('public_visibility')
    #         savedata = registerForm(domain=domain,username=username , email=email , password=password,visibility=visibility)
    #         savedata.save()
    #         user = registerForm(
    #             username=form.cleaned_data['username'],
    #             email=form.cleaned_data['email'],
    #             password=form.cleaned_data['password']
    #         )
    #         # Log in the user after registration if needed
    #         # login(request, user)
    #         msg="Registration Sucessfull"
    #         data={"msg":msg}
    #         return render(request,'login.html',data)  # Redirect to login page after successful registration
    # else:
    #     form = RegisterForm()

    # return render(request, 'login.html', {'form': form})

def reg(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")


def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)
        if user is not None:
            print("log page")
            return render(request,'Dashboard.html')
        else:
            a="invalid credential"
            return HttpResponse("Invalid Login Details")
            
       
    
def userpage(request):
    users = registerForm.objects.all()
    data={"users":users}
    return render(request,"userPage.html",data)

@login_required
def dashboard(request):
    print("dashboard")
    return render(request,"Dashboard.html")
    
def authorpage(request):
    
    author = registerForm.objects.filter(domain="Author",visibility=True)
    data={"domain":author}
    
    print(author)
    return render(request,"authorspage.html",data)
        
   

def sellerpage(request):
    seller = registerForm.objects.filter(domain="Seller",visibility=True)
    
    data = {"domain":seller}
    
    return render(request,'sellerpage.html',data)
    

 
def uploadFile(request):
    files = request.POST.get('file')
    
    store = UploadFiles(files=files)
    store.save()
    
    return render(request,"uploadFiles.html")

@csrf_exempt

def auth(request):
    username=request.POST.get('username')
    email = request.POST.get('email')
    password=request.POST.get('password')
    domain=request.POST.get('domain')
    visibility = request.POST.get('public_visibility')
   
    
    if visibility=="on":
        print(visibility)
        visibility=True
    else:
        print(visibility)
        visibility=False
         
    user = User.objects.create_user(username=username,
                                         password=password,
                                         email=email)
    
    user.save()
    store = registerForm(username=username,email=email,domain=domain,visibility=visibility)
    store.save()
    #log(username,password)
    return redirect('login')

def logoutss(request):
    logout(request)
    return redirect("login")

def show_uploads(request):
    file = UploadFiles.objects.all()
    data={"file":file}
    return render(request,'showUploadFile.html',data)
    
    
import psycopg2
from psycopg2 import sql

# Replace these values with your actual database credentials
db_config = {
    'host': 'localhost',
    'database': 'todo',
    'user': 'mustafabohra',
    'password': 'mustafabohra',
    'port': '5432',  # Usually 5432 for PostgreSQL
}

def fetch_data_from_database():
    try:
        connection = psycopg2.connect(**db_config)

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM form_registerform")
        
        result = cursor.fetchall()
        print({'result':result})
        return result
        

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example SQL query


result=fetch_data_from_database()

def create_dbFrame(sql_queary):
    coloumn = ['id','username','email','password','domain','visibility']
    df = pd.DataFrame(sql_queary,columns=coloumn)
    print(df)
    
create_dbFrame(result)
    





