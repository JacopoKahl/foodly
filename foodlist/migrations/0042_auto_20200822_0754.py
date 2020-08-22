# Generated by Django 3.0.9 on 2020-08-22 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlist', '0041_auto_20200822_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlist',
            name='todayIs',
            field=models.DateField(blank=True, default=datetime.datetime.now, help_text='This will be helpful to calculate the expiration date', verbose_name='Today is'),
        ),
    ]
