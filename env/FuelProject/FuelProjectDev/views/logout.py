from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout


def logout_page(request):
    logout(request)

    return HttpResponseRedirect("index")
