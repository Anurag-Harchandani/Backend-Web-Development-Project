# Generated by Django 5.0.4 on 2024-05-07 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_order_dish_order_price_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Dish',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Quantity',
        ),
    ]
