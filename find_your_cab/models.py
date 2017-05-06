import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class CabUser(models.Model):
    name_user = models.CharField(max_length=100,default='')
    password_user = models.IntegerField(default=0)

    def __str__(self):
        return self.name_user

    def __int__(self):
        return self.password_user

class CabDriver(models.Model):
    name_driver = models.CharField(max_length=100,default='')
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.name_driver

    def __int__(self):
        return self.point

class DriverHistory(models.Model):
    cab_driver = models.ForeignKey(CabDriver, on_delete=models.CASCADE)
    cab_user = models.CharField(max_length=100,default='')
    driv_point = models.FloatField(default=0)

    def __str__(self):
        return self.cab_user

    def __flo__(self):
        return self.driv_point
