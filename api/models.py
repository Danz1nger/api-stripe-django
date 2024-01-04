from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=255, choices=[(STRIPE_CURRENCY, STRIPE_CURRENCY), (STRIPE_CURRENCY_TWO, STRIPE_CURRENCY_TWO)])

class Order(models.Model):
    items = models.ManyToManyField(Item)
    # Other fields

class Discount(models.Model):
   percentage = models.DecimalField(max_digits=5, decimal_places=2)

class Tax(models.Model):
   rate = models.DecimalField(max_digits=5, decimal_places=2)