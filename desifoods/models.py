from django.db import models
import datetime


class contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)



class Product(models.Model):
    image = models.ImageField(upload_to='photos', null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=0.0,null=True)
    description = models.TextField(null=True)



class CustomerOrder(models.Model):
    image = models.ImageField(upload_to='order/photos', default="", null=True)
    product = models.CharField(max_length=100, default='', null=True)
    quantity = models.CharField(max_length=200, default='', null=True)
    address = models.TextField(default="", null=True)
    price = models.FloatField(default=0.0, null=True)
    phone = models.CharField(max_length=30, default="", null=True)
    total = models.IntegerField(default=0, null=True)
    date = models.DateField(default=datetime.date.today, null=True)
    customer_name = models.CharField(max_length=100, default='', null=True)