# Generated by Django 3.0.7 on 2020-06-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_recipe_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_pic',
            field=models.ImageField(blank=True, default='', upload_to='recipe_pics'),
        ),
    ]