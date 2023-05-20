from django.db import models
from django.contrib.auth.models import User
from Cars.models import Car_shop


class Seller_passport(models.Model):
    passport_series = models.IntegerField()
    passport_number = models.IntegerField()
    issue_date = models.CharField(max_length=15)
    issued_by = models.CharField(max_length=50)

    def __str__(self):
        return str(self.passport_series) + ' ' + str(self.passport_number)


class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    passport = models.ForeignKey(Seller_passport, null=True, on_delete=models.CASCADE, blank=True)
    dealer = models.ForeignKey(Car_shop, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.user.username
