from django.db import models
from django.utils.timezone import now

class Expense(models.Model):
    date = models.DateTimeField(default=now)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    cash = models.BooleanField(default=True)

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
