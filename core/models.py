from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price',decimal_places=2, max_digits=8)
    stock = models.IntegerField('Stock Quantity')

    def __str__(self):
        return self.name

class Client(models.Model):
    firstName = models.CharField('Firstname', max_length=100)
    lastName = models.CharField('Lastname', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'