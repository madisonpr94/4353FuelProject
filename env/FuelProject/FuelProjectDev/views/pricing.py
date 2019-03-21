from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
import json


def price_module(request):
    gallons = float(request.GET["gallons"])

    # Placeholder! Replace with pricing module in Assignment 4
    price_per_gallon = 1.71
    total_price = '{0:.2f}'.format(round(gallons * price_per_gallon, 2))

    price = {
        'gallons_requested': gallons,
        'price_per_gallon': price_per_gallon,
        'total_price': total_price
    }
    data = json.dumps(price)

    return HttpResponse(data, content_type='application/json')
