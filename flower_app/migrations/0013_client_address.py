# Generated by Django 4.2.4 on 2023-08-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_app', '0012_alter_order_date_alter_order_delivery_time_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес'),
        ),
    ]
