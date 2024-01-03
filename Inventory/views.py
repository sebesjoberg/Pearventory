from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from django.db.models import F, Sum, Case, When, IntegerField
from .forms import DeliveryForm

# Create your views here.
from .models import Delivery, Site, Storage, Product


def index(request):
    output = Delivery.objects.values(
        "site__site__name", "site__product__name"
    ).annotate(
        stock=Sum(
            Case(
                When(deliveryType="IN", then=F("amount")),
                default=0,
                output_field=IntegerField(),
            )
        )
        - Sum(
            Case(
                When(deliveryType="OUT", then=F("amount")),
                default=0,
                output_field=IntegerField(),
            )
        )
    )

    stock_by_site = {}

    # Organizing output into a dictionary
    for entry in output:
        site_name = entry["site__site__name"]
        product_name = entry["site__product__name"]
        stock = entry["stock"]

        if site_name not in stock_by_site:
            stock_by_site[site_name] = {}

        stock_by_site[site_name][product_name] = stock

    template = loader.get_template("inventory/index.html")
    context = {"stocks": stock_by_site}
    return HttpResponse(template.render(context, request))


def delivery(request):
    storages = Storage.objects.all()
    grouped_deliveries = {}

    for storage in storages:
        deliveries_to_storage = Delivery.objects.filter(site=storage).order_by("-date")
        if storage.site.name not in grouped_deliveries:
            grouped_deliveries[storage.site.name] = {}

        deliveries = list(deliveries_to_storage)
        balance = 0
        for delivery in deliveries:
            if delivery.deliveryType == "IN":
                balance += delivery.amount
            elif delivery.deliveryType == "OUT":
                balance -= delivery.amount

        grouped_deliveries[storage.site.name][storage.product.name] = {
            "deliveries": deliveries,
            "balance": balance,
        }
    template = loader.get_template("inventory/delivery.html")
    context = {"grouped_deliveries": grouped_deliveries}
    return HttpResponse(template.render(context, request))


def adddelivery(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.save()

            return redirect("index")
    else:
        form = DeliveryForm()
    template = loader.get_template("inventory/add_delivery.html")
    context = {"form": form}
    return HttpResponse(template.render(context, request))
