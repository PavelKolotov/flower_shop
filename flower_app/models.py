from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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


class BouquetQuerySet(models.QuerySet):
    def get_price_category(self, category, reason):
        if not category.min and not category.max:
            price_category = self.filter(reason=reason)
        elif not category.min:
            price_category = self.filter(price__lte=category.max, reason=reason)
        elif not category.max:
            price_category = self.filter(price__gt=category.min, reason=reason)
        else:
            price_category = self.filter(price__gt=category.min, price__lte=category.max, reason=reason)
        return price_category


class Bouquet(models.Model):
    title = models.CharField('Название', max_length=100, null=True)
    price = models.FloatField('Цена')
    composition = HTMLField('Состав')
    size = models.CharField('Размер', max_length=100, blank=True, null=True)
    description = HTMLField('Описание', blank=True, null=True)
    image = models.ImageField('Картинка', blank=True, null=True)
    assortment = models.BooleanField('В наличии', default=True)
    reason = models.ForeignKey('Reason', on_delete=models.CASCADE, related_name='bouquets')

    objects = BouquetQuerySet.as_manager()

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

    delivery_address = models.CharField('Адрес доставки', max_length=200, null=True, blank=True,)

    def __str__(self):
        return f'Заказ №{self.id}'

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'


class PriceCategory(models.Model):
    title = models.CharField('Ценовая категория', max_length=100,)
    min = models.IntegerField('Минимальная цена', blank=True, null=True)
    max = models.IntegerField('Максимальная цена', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории цен'


class Consultation(models.Model):

    class Status(models.TextChoices):
        UNPROCESSED = "UN", _("Не обработана")
        COMPLETED = "OK", _("Выполнена")

    status = models.CharField(
        verbose_name="статус",
        max_length=2,
        choices=Status.choices,
        default=Status.UNPROCESSED,
        db_index=True
    )
    client = models.ForeignKey(
        'Client',
        on_delete=models.CASCADE,
        verbose_name='Клиент',
        related_name='consultations',
        null=True
    )
    date = models.DateTimeField('Дата подачи', default=timezone.now)

    def __str__(self):
        return f'{self.client.name} {self.client.phone}'

    class Meta:
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультацию'
