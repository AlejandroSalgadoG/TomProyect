from datetime import datetime

from django.db import models

date_format = '%d/%m/%Y-%H:%M:%S'

class Bill(models.Model):
    date = models.DateField(default=datetime.now())
    total = models.IntegerField(default=0)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
