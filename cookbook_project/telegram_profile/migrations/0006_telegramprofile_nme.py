# Generated by Django 3.0.7 on 2020-06-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_profile', '0005_auto_20200621_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramprofile',
            name='nme',
            field=models.CharField(blank=True, default='', max_length=200, unique=True),
        ),
    ]
