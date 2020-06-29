# Generated by Django 3.0.7 on 2020-06-21 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('telegram_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramprofile',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='userid', to=settings.AUTH_USER_MODEL),
        ),
    ]