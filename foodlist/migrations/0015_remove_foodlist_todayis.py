# Generated by Django 3.0.9 on 2020-08-09 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodlist', '0014_auto_20200809_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodlist',
            name='todayIs',
        ),
    ]
