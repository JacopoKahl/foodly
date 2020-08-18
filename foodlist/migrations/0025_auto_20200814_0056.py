# Generated by Django 3.0.9 on 2020-08-13 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlist', '0024_auto_20200813_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlist',
            name='todayIs',
            field=models.DateField(blank=True, default=datetime.datetime.now, help_text='Check if the product is good to eat', verbose_name='Today is'),
        ),
    ]
