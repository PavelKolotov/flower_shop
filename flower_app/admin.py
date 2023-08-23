from django.contrib import admin

from flower_app import models

# Register your models here.


class BouquetOrderInline(admin.TabularInline):
    extra = 1
    model = models.BouquetOrder


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ['name', 'phone']
    list_display = ['name', 'phone']


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
    fields = ['title', 'price', 'composition', 'description', 'image', 'assortment', 'reason']
    list_display = ['title', 'price', 'reason', 'assortment']
    list_filter = ['reason__title',]


@admin.register(models.Reason)
class ReasonAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ['title',]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['client', 'status', 'date']
    inlines = [BouquetOrderInline,]
    search_fields = ['client__id',]
    list_filter = ['date', 'status']
    list_display = ['client_id', 'id', 'status', 'date']
