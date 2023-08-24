from django import forms
from .models import Order
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Номер телефона должен быть введен в формате: '+79999999999'. Максимум 15 знаков разрешено."
)


class OrderForm(forms.ModelForm):
    tel = forms.CharField(validators=[phone_regex], max_length=17)

    class Meta:
        model = Order
        fields = ['client', 'status', 'date', 'staff', 'delivery_time_slot', 'tel']