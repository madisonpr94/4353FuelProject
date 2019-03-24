from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Context, loader


def logout_page(request):
    # To Do: Clear user session and ensure user is completely logged out
    return HttpResponseRedirect("index")
