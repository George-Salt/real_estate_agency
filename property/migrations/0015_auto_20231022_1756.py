# Generated by Django 2.2.24 on 2023-10-22 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20231022_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='owner',
            new_name='owner_name',
        ),
    ]
