from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from  django.contrib import messages
import time
# Create your views here.

def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        allowed_domains = ['gmail.com', 'yahoo.com', 'mnk.gcs']
        domain = email.split('@')[-1]
        
        if User.objects.filter(username = username).exists():
            messages.error(request,"User Name already exists")
            return redirect('register')
        
        elif domain not in allowed_domains:
            messages.error(request, "Only Gmail, Yahoo, and mnk.gcs emails are allowed.")
            return redirect('register')
        
        elif User.objects.filter(email = email).exists():
            messages.error(request,"Email already exists")
            return redirect('register')
        
        elif not password == confirm_password:
            messages.error(request,"Type same password for both")
            return redirect('register')
        
        if domain not in allowed_domains:
            messages.error(request, "Only Gmail, Yahoo, and mnk.gcs emails are allowed.")
            return redirect('register')
        else:
            
            user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
            user.save()
            messages.info(request,"User Registered Successfully")
            return redirect('login')
    else:
        return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password = password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,"login.html")
    
    
def logout(request):
    auth.logout(request)
    messages.info(request,'logged Out Successfully')
    return redirect('/')
        