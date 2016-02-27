from __future__ import unicode_literals
from django.db import models

class Invoice(models.Model):
    customer = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    total_quantity = models.IntegerField()
    total_amount = models.FloatField()


class Transaction(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    line_total = models.FloatField()
    invoice = models.ForeignKey(Invoice, related_name='transactions' ,default='')
