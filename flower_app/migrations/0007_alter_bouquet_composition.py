# Generated by Django 4.2.4 on 2023-08-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_app', '0006_alter_reason_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='composition',
            field=models.TextField(verbose_name='Состав'),
        ),
    ]
