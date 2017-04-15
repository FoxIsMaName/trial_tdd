import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class CabUser(models.Model):
    name_user = models.CharField(max_length=100,default='')
    id_user = models.IntegerField(default=0)
    date_user = models.DateTimeField('date published')

    def __str__(self):
        return self.name_user

    def __int__(self):
        return self.id_user

    def __str__(self):
        return self.date_user

class CabDriver(models.Model):
    name_driver = models.CharField(max_length=100,default='')
    id_driver = models.IntegerField(default=0)
    date_driver = models.DateTimeField('date published')
    point = models.IntegerField(default=0)
    cab_user = models.ForeignKey(CabUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_driver

    def __int__(self):
        return self.id_driver

    def __str__(self):
        return self.date_driver

    def __int__(self):
        return self.point
