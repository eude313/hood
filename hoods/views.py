from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from hoods.models import Users
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from hoods.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'hod/home.html')


def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        confirm_password= request.POST['confirm_password']
        if password == confirm_password:
            user = Users(username=username, email=email, password=make_password(password))
            user.save()
            messages.add_message(request, messages.SUCCESS, "Account created successfully!")
            return redirect('signIn')
    else:
        return render(request, 'auth/register.html')

def signIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, "invalid infomation!") 
            return redirect("signIn") 
    else:
        return render(request, 'auth/signIn.html')

def signOut(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "logg Out successfull!")
    return redirect('signIn')


def profile(request):
    
    return render(request, 'hod/profile.html')

def bussiness(request):
    
    return render(request, 'hod/bussiness.html')
