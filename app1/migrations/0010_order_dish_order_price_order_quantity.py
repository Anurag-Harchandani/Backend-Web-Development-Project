# Generated by Django 5.0.4 on 2024-05-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_remove_order_dish_remove_order_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Dish',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='Price',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='Quantity',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
