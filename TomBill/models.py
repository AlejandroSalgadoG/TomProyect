from django.db import models
from django.utils.timezone import now

date_format = '%d/%m/%Y-%H:%M:%S'

class Section(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50)
    short = models.CharField(max_length=25)
    html = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

class Bill(models.Model):
    date = models.DateTimeField(default=now)
    name = models.CharField(max_length=50)
    cash = models.BooleanField(default=True)
    subtotal = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

class Purchase(models.Model):
    quantity = models.IntegerField(default=0)
    free = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
