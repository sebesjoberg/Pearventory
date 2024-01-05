from django import forms
from django.core.validators import MinValueValidator

from .models import Delivery


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ["site", "amount", "deliveryType", "date"]
        widgets = {
            "date": forms.DateInput(
                attrs={"class": "form-control", "id": "datepicker"}
            ),
        }
        validators = {
            "amount": [
                MinValueValidator(1, message="Amount must be greater than zero.")
            ],
        }
