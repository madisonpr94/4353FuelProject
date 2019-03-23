from django.shortcuts import render, redirect, render_to_response
from django.http import *
from django.template import Context, loader, RequestContext
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index_page(request):
    return render(request, 'FuelProjectDev/index.html')

def login_page(request):
    return render(request, 'FuelProjectDev/login.html')

def profile_page(request):
    return render(request, 'FuelProjectDev/profile.html')

def check_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                return render(request, 'FuelProjectDev/profile.html')
    return render(request, 'FuelProjectDev/index.html')


    
    
