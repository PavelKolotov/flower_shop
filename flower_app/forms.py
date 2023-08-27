from django import forms
from django.core.validators import RegexValidator
from .models import Order, DeliveryTimeSlot, Consultation


phone_regex = RegexValidator(
    regex=r'^(8|\+7)\d{10}$',
    message='Телефонный номер введен некорректно'
)


class OrderForm(forms.ModelForm):
    fname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'order__form_input',
            'placeholder': 'Введите Имя'
        })
    )
    tel = forms.CharField(
        validators=[phone_regex],
        widget=forms.TextInput(attrs={
            'class': 'order__form_input',
            'placeholder': '+ 7 (999) 000 00 00'
        }),
        error_messages={
            'invalid': 'Телефонный номер введен некорректно'
        }
    )
    adres = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'order__form_input',
            'placeholder': 'Адрес доставки'
        })
    )
    orderTime = forms.ModelChoiceField(
        queryset=DeliveryTimeSlot.objects.all(),
        widget=forms.RadioSelect(attrs={'class': 'order__form_radio'}),
        required=True
    )

    class Meta:
        model = Order
        fields = ['fname', 'tel', 'adres', 'orderTime']


class ConsultationForm(forms.ModelForm):
    fname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'consultation__form_input',
            'placeholder': 'Введите Имя'
        })
    )
    tel = forms.CharField(
        validators=[phone_regex],
        widget=forms.TextInput(attrs={
            'class': 'consultation__form_input',
            'placeholder': '+ 7 (999) 000 00 00'
        }),
        error_messages={
            'invalid': 'Телефонный номер введен некорректно'
        }
    )


    class Meta:
        model = Consultation
        fields = ['fname', 'tel']
