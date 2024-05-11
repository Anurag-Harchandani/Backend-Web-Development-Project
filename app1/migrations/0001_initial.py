# Generated by Django 5.0.4 on 2024-05-04 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dish', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('Total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Phone_Number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
            ],
        ),
    ]