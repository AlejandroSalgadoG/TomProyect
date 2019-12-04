from django.db import models
from django.utils.timezone import now

class Base(models.Model):
    date = models.DateTimeField(default=now)
    value = models.IntegerField(default=0)
