from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField
from django.utils import timezone


class Reason(models.Model):
    title = models.CharField('Повод', max_length=50)
    description = HTMLField('Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Повод'
        verbose_name = 'Повод'


class DeliveryTimeSlot(models.Model):
    title = models.CharField('Временной интервал', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Временные интервалы'
        verbose_name = 'Временной интервал'


class Bouquet(models.Model):
    title = models.CharField('Название', max_length=100, null=True)
    price = models.FloatField('Цена')
    composition = HTMLField('Состав')
    size = models.CharField('Размер', max_length=100, blank=True, null=True)
    description = HTMLField('Описание', blank=True, null=True)
    image = models.ImageField('Картинка', blank=True, null=True)
    assortment = models.BooleanField('В наличии', default=True)
    reason = models.ForeignKey('Reason', on_delete=models.CASCADE, related_name='bouquets')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Букеты'
        verbose_name = 'Букет'


class Staff(models.Model):
    name = models.CharField('ФИО', max_length=200)
    telegram = models.BigIntegerField('Telegram id', blank=True, null=True)
    phone = PhoneNumberField('Телефон', unique=True, null=True)
    role = models.CharField('Роль', max_length=50)

    def __str__(self):
        return f'{self.name} - {self.role} '

    class Meta:
        verbose_name_plural = 'Персонал'
        verbose_name = 'Сотрудник'


class Client(models.Model):
    name = models.CharField('ФИО', max_length=200)
    phone = PhoneNumberField('Телефон', unique=True, null=True)
    address = models.CharField('Адрес', max_length=200, null=True, blank=True,)

    def __str__(self):
        return f'{self.phone} {self.name}'

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'


class BouquetOrder(models.Model):
    bouquet = models.ForeignKey(
        'Bouquet',
        on_delete=models.SET_NULL,
        null=True,
        related_name='bouquet_orders',
    )
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name='bouquet_orders',
    )
    quantity = models.PositiveIntegerField('Количество')


class Order(models.Model):
    client = models.ForeignKey(
        'Client',
        verbose_name='клиент',
        related_name='orders',
        on_delete=models.CASCADE,
    )
    bouquets = models.ManyToManyField(
        'Bouquet',
        through=BouquetOrder,
        related_name='orders'
    )
    date = models.DateTimeField('Дата', default=timezone.now)
    status = models.BooleanField('Выполнено', default=False)
    staff = models.ForeignKey(
        'Staff',
        verbose_name='Флорист',
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    delivery_time_slot = models.ForeignKey(
        'DeliveryTimeSlot',
        verbose_name='Временной интервал',
        related_name='delivery_orders',
        on_delete=models.CASCADE,
        null=True)

    def __str__(self):
        return f'Заказ №{self.id}'

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
