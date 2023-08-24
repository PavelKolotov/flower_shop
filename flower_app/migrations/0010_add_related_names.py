# Generated by Django 4.2.4 on 2023-08-24 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flower_app', '0009_use_tinymce'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='flower_app.staff', verbose_name='Флорист'),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='reason',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bouquets', to='flower_app.reason'),
        ),
        migrations.AlterField(
            model_name='bouquetorder',
            name='bouquet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bouquet_orders', to='flower_app.bouquet'),
        ),
        migrations.AlterField(
            model_name='bouquetorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bouquet_orders', to='flower_app.order'),
        ),
    ]