# Generated by Django 5.0.4 on 2024-05-04 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='Total',
        ),
    ]
