# Generated by Django 5.0.4 on 2024-05-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_cart_quantity_remove_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
