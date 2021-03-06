# Generated by Django 3.0.7 on 2020-06-21 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_chat_id', models.CharField(blank=True, default='', max_length=40, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
