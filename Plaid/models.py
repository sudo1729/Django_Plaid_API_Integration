from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

# Create your models here.


class PlaidItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE, default=None)
    access_token = models.CharField(max_length=200, unique=True)
    item_id = models.CharField(max_length=200, unique=True)


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    plaid_account_id = models.CharField(max_length=200, null=True, unique=True)
    balances = models.JSONField(null=True)
    mask = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    official_name = models.CharField(max_length=200, null=True)
    subtype = models.CharField(max_length=200, null=True)
    account_type = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(PlaidItem, on_delete=models.CASCADE, default=None, null=True, blank=True)
