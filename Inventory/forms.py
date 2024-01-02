from django import forms


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
