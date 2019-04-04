from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import random

from ..models.past_order import PastOrder

msg_no_entries = "No order history was found."


@login_required
def history_page(request):
    context = {}
    context["t"] = 0

    if "t" in request.GET:
        context["t"] = int(request.GET["t"])

    itemsPerPage = 10  # Constant
    context["itemsPerPage"] = itemsPerPage
    context["prevT"] = max(context["t"] - itemsPerPage, 0)
    context["nextT"] = context["t"] + itemsPerPage

    try:
        if request.user.has_perm('FuelProjectDev.admin_rights'):
            models = PastOrder.objects.all()
        else:
            models = PastOrder.objects.filter(
                user_id=request.user.id).order_by("id")
    except PastOrder.DoesNotExist:
        models = []

    if len(models) == 0:
        context["no_entries"] = True
        context["msg_no_entries"] = msg_no_entries

    usernames = {}
    for m in models:
        if m.user_id not in usernames.keys():
            usernames[m.user_id] = User.objects.get(id=m.user_id).username

    context['usernames'] = usernames
    context["canSeekNext"] = (context["nextT"] < len(models))
    context["entries"] = models[context["t"]:context["nextT"]]

    if not context["canSeekNext"]:
        context["nextT"] = context["t"]

    return render(request, 'FuelProjectDev/order_history.html', context)


@register.filter
def get_item(dict, key):
    return dict.get(key)
