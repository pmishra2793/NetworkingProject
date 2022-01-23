# Generated by Django 4.0.1 on 2022-01-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0002_rename_hoopback_routerdetails_loopback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routerdetails',
            name='hostname',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='routerdetails',
            name='loopback',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='routerdetails',
            name='mac_address',
            field=models.CharField(max_length=17, unique=True),
        ),
        migrations.AlterField(
            model_name='routerdetails',
            name='sap_id',
            field=models.CharField(max_length=18, unique=True),
        ),
    ]
