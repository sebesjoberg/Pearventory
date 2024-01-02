from django.db import models
from datetime import date

# Create your models here.
# vi har sites(platser), produkter
# sen har vi lagerplats, en lagerplats har en site,
# en produkttyp och ett antal
# vi kan också ha leveranser som då har en lagerplats
# typ(in/ut) och antal


class Delivery(models.Model):
    TYPE_CHOICES = {
        "IN": "Indelivery",
        "OUT": "Outdelivery",
    }
    site = models.ForeignKey("Storage", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    deliveryType = models.CharField(max_length=3, choices=TYPE_CHOICES)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.site) + ", " + str(self.deliveryType) + ", " + str(self.amount)


class Storage(models.Model):
    site = models.ForeignKey("Site", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site) + ", " + str(self.product)


class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
