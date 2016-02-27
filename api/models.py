from __future__ import unicode_literals
from django.db import models

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=100)
    date = models.DateField()
    total_quantity = models.IntegerField()
    total_amount = models.FloatField()


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    line_total = models.FloatField()
    Invoice_id = models.IntegerField()
