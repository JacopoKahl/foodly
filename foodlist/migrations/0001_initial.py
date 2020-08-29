# Generated by Django 3.0.9 on 2020-08-29 20:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(help_text='The name of the product', max_length=30, verbose_name='Product name')),
                ('productStatus', models.CharField(choices=[('good', 'GOOD'), ('expired', 'EXPIRED')], default='good', max_length=10, verbose_name='Product status')),
                ('productCategory', models.CharField(choices=[('meat', 'MEAT'), ('fish', 'FISH'), ('fruit', 'FRUIT'), ('vegetables', 'VEGETABLES'), ('pasta', 'PASTA'), ('cheese', 'CHEESE')], default='meat', help_text='The type of food', max_length=10, verbose_name='Product category')),
                ('productExpDate', models.DateField(help_text='Food Expiration Dates', verbose_name='Expiring day')),
                ('todayIs', models.DateField(blank=True, default=datetime.date.today, help_text='This will be helpful to calculate the expiration date', verbose_name='Today is')),
                ('productPrice', models.DecimalField(decimal_places=2, help_text='The price of the single product', max_digits=10, verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(to='foodlist.FoodList')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
