from django.contrib import admin
from flower_app import models


class BouquetOrderInline(admin.TabularInline):
    extra = 1
    model = models.BouquetOrder


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ['name', 'phone', 'address']
    list_display = ['name', 'phone', 'address']


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    fields = ['name', 'telegram', 'role', 'phone']
    list_display = ['role', 'name']
    list_filter = ['role',]
    search_fields = ['phone',]
    search_help_text = 'Поиск по номеру телефона'


@admin.register(models.BouquetOrder)
class BouquetOrderAdmin(admin.ModelAdmin):
    fields = ['bouquet', 'quantity', 'order']
    list_display = ['order_id', ]


@admin.register(models.Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    fields = ['title', 'price', 'composition', 'size', 'description', 'image', 'assortment', 'reason']
    list_display = ['title', 'price', 'reason', 'assortment']
    list_filter = ['reason__title',]


@admin.register(models.Reason)
class ReasonAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ['title', ]


@admin.register(models.DeliveryTimeSlot)
class DeliveryTimeSlotAdmin(admin.ModelAdmin):
    fields = ['title', ]
    list_display = ['title', ]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['client', 'status', 'date', 'staff', 'delivery_time_slot', 'delivery_address']
    inlines = [BouquetOrderInline]
    search_fields = ['client__id',]
    search_help_text = 'Поиск по id клиента'
    list_filter = ['date', 'status', 'staff']
    list_display = ['client_id', 'id', 'status', 'date']
