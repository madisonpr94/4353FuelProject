from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    if check_login(request):
        return render(request, 'FuelProjectDev/profile.html')
    else:
        context = {}
        if request.POST:
            context["login_error"] = True
            context["error_msg"] = "Invalid username or password."
        return render(request, 'FuelProjectDev/login.html', context)


def check_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                return True
    return False
