from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_page(request):
    if check_login(request):
        if "next" in request.GET:
            return HttpResponseRedirect(request.GET["next"])
        return HttpResponseRedirect('profile')

    else:
        context = {}

        reg_chk = check_register(request)
        if reg_chk[0]:
            context["register_success"] = True
        elif reg_chk[1] is not None:
            context["login_error"] = True
            context["error_msg"] = reg_chk[1][1]

        else:
            if request.POST:  # Login form submitted
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
        if "username" and "password" in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return True
    return False


def check_register(request):
    # Returns an object (Bool, (Bool, String))
    # (Registration Success, (Registration Error, Error Message))

    if request.POST:
        if "username-register" and "password-register" and "password-confirm" in request.POST:
            username = request.POST['username-register']
            password = request.POST['password-register']
            password_confirm = request.POST['password-confirm']

            if password != password_confirm:
                return (False, (True, "Passwords do not match."))

            if User.objects.filter(username=username).exists():
                # Username already exists
                return (False, (True, "That username is unavailable."))

            user = User.objects.create_user(username, None, password)
            user.save()
            return (True, (False, None))

    return (False, None)
