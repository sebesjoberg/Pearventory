from django.db import models
from datetime import date
from django.core.validators import MinValueValidator


class Delivery(models.Model):
    TYPE_CHOICES = {
        "IN": "Indelivery",
        "OUT": "Outdelivery",
    }
    site = models.ForeignKey("Storage", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, validators=[MinValueValidator(1)])
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
