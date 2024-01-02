from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse(
        "Hello, world. You're at the Inventory index. here we should see stock of all the items at the different sites"
    )


def delivery(request):
    return HttpResponse(
        "Hello, world. You're at the delivery, here we should see all deliveries, be able to filter by both product and site"
    )


def adddelivery(request):
    return HttpResponse(
        "Hello, world. You're at the add delivery, here we should be able to add a new delivery"
    )
