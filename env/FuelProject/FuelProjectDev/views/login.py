from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout

def login_page(request):
    return render(request, 'FuelProjectDev/login.html')

def check_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                return render(request, 'FuelProjectDev/profile.html')
    return render(request, 'FuelProjectDev/index.html')