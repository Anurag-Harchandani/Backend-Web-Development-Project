# Generated by Django 5.0.4 on 2024-05-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Price',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Quantity',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='Email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='Phone_Number',
            field=models.TextField(),
        ),
    ]
