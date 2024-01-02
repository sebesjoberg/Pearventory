from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("delivery/", views.delivery, name="delivery"),
    path("delivery/add", views.adddelivery, name="adddelivery"),
]
