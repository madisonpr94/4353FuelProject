from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
import random


def create_random_entry(n):  # Create entries for page testing
    # This will be replaced with database lookup in Assignment 4
    num = n

    gallons = random.randrange(500, 25000, step=100)

    address = str(random.randrange(10, 9999))
    address += " Example St. Houston, TX 77024"

    delivery_date = str(random.randrange(1, 12)) + "/"
    delivery_date += str(random.randrange(1, 31)) + "/"
    delivery_date += str(random.randrange(2020, 2024))

    price_per_gallon = (1 + (2 * random.random()))
    total_price = "$" + '{0:.2f}'.format(gallons * price_per_gallon)
    price_per_gallon = "$" + '{0:.2f}'.format(price_per_gallon)

    entry = (str(num), str(gallons), address, delivery_date, price_per_gallon,
             total_price)
    return entry


@login_required
def history_page(request):
    context = {}
    context["t"] = 0
    context["username"] = request.user.username

    if "t" in request.GET:
        context["t"] = int(request.GET["t"])

    itemsPerPage = 10  # Constant
    context["itemsPerPage"] = itemsPerPage
    context["prevT"] = max(context["t"] - itemsPerPage, 0)
    context["nextT"] = context["t"] + itemsPerPage

    models = []
    for i in range(50):
        entry = create_random_entry(i)
        models.append(entry)

    context["canSeekNext"] = (context["nextT"] < len(models))
    context["entries"] = models[context["t"]:context["nextT"]]

    if not context["canSeekNext"]:
        context["nextT"] = context["t"]

    return render(request, 'FuelProjectDev/order_history.html', context)
