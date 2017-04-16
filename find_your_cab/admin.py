from django.contrib import admin
from .models import CabUser, CabDriver

# Register your models here.

admin.site.register(CabUser)
admin.site.register(CabDriver)
