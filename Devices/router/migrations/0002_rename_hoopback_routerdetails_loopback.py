# Generated by Django 4.0.1 on 2022-01-22 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routerdetails',
            old_name='hoopback',
            new_name='loopback',
        ),
    ]