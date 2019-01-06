from django.contrib import admin
from login.models import Account
from dashboard.models import Slot

admin.site.register(Account)
admin.site.register(Slot)