# Generated by Django 5.0.4 on 2024-05-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_cart_price_alter_cart_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dishname', models.CharField(max_length=100)),
                ('Price', models.TextField()),
                ('Image', models.FileField(upload_to='')),
            ],
        ),
    ]
