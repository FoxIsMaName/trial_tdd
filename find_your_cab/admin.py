from django.contrib import admin
from django.contrib.auth.models import User
from .models import CabUser, CabDriver, DriverHistory

# Register your models here.


admin.site.register(CabDriver)
admin.site.register(DriverHistory)
