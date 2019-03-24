from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    if check_login(request):
        if "next" in request.GET:
            return HttpResponseRedirect(request.GET["next"])
        return HttpResponseRedirect('profile')
    else:
        context = {}

        if request.POST:  # Form submitted
            context["login_error"] = True
            context["error_msg"] = "Invalid username or password."

        context["action"] = "login"
        if "next" in request.GET:
            context["action"] += "?next=" + request.GET["next"]
            context["login_error"] = True
            context["error_msg"] = "You must log in first."

        return render(request, 'FuelProjectDev/login.html', context)


def check_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return True
    return False
