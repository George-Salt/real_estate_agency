# Generated by Django 2.2.24 on 2023-10-22 12:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20231007_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кому понравилось'),
        ),
    ]
