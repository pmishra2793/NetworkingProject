from django.db import models

# Create your models here.

class RouterDetails(models.Model):
    sap_id = models.CharField(max_length=18, blank=False, unique=True)
    hostname = models.CharField(max_length=14, blank=False, unique=True)
    # loopback = models.CharField(max_length=20, blank=False, unique=True)
    loopback = models.GenericIPAddressField(blank=False, unique=True)
    mac_address = models.CharField(max_length=17, blank=False, unique=True)
