# Generated by Django 3.0.9 on 2020-08-22 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlist', '0040_auto_20200822_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlist',
            name='todayIs',
            field=models.DateField(auto_now_add=True, help_text='This will be helpful to calculate the expiration date', verbose_name='Today is'),
        ),
    ]
