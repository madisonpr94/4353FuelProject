from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout


def logout_page(request):
    # To Do: Clear user session and ensure user is completely logged out
    logout(request)

    return HttpResponseRedirect("index")
