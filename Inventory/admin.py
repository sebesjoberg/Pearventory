from django.contrib import admin

# Register your models here.


from .models import Storage, Site, Product, Delivery

admin.site.register([Storage, Site, Product, Delivery])
