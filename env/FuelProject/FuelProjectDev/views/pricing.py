from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
import json


@login_required
def price_module(request):

    gallons = float(request.GET["gallons"])
    delivery_date = datetime.strptime(request.GET["date"], "%Y-%m-%d")

    delta = delivery_date - datetime.today()
    if delta.days < 1:
        return HttpResponse(None, status='500')

    # Placeholder! Replace with pricing module in Assignment 4
    price_per_gallon = round(1.71 + (0.05 * delta.days), 2)
    total_price = '{0:.2f}'.format(round(gallons * price_per_gallon, 2))
    price_per_gallon = '{0:.2f}'.format(price_per_gallon)

    price = {
        'gallons_requested': gallons,
        'price_per_gallon': price_per_gallon,
        'total_price': total_price
    }
    data = json.dumps(price)

    return HttpResponse(data, content_type='application/json')
