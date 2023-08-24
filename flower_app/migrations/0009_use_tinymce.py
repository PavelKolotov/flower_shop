# Generated by Django 4.2.4 on 2023-08-24 08:27

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_app', '0008_bouquet_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='composition',
            field=tinymce.models.HTMLField(verbose_name='Состав'),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='reason',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]