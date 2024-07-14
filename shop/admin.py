# En shop/admin.py

from django.contrib import admin
from .models import RankedAccount,Comuna

admin.site.register(RankedAccount)
admin.site.register(Comuna)