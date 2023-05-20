import datetime
from django.db import models
from django.contrib.auth.models import User


class Firm(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car_passport(models.Model):
    category = models.CharField(max_length=5)
    body_type = models.CharField(max_length=30)
    passport_series = models.CharField(max_length=10)
    passport_number = models.CharField(max_length=10)
    weight = models.FloatField()
    engine_power = models.IntegerField()

    def __str__(self):
        return self.passport_series + ' ' + self.passport_number + ' - ' + self.body_type


class Car(models.Model):
    model = models.ForeignKey(Firm, null=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey('Auth.Seller', null=True, on_delete=models.SET_NULL)
    price = models.IntegerField()
    city = models.CharField(max_length=40)
    passport = models.ForeignKey(Car_passport, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.model.name + ' ' + str(self.price) + 'руб'


class Car_shop(models.Model):
    address = models.CharField(max_length=100)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)

    def __str__(self):
        return self.firm.name + ' ' + self.address


class Sale(models.Model):
    buyer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.buyer.username + ' ' + self.car.model.name


