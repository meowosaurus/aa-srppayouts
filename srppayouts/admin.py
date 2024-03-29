"""Admin models"""

# Django
from django.contrib import admin 

from .models import *

# Adding search bars to admin panel
class ShipAdmin(admin.ModelAdmin):
    search_fields = ['name']

class PayoutAdmin(admin.ModelAdmin):
    search_fields = ['ship__name']

class ReimbursementAdmin(admin.ModelAdmin):
    search_fields = ['name']

# Register your models here.
admin.site.register(Ship, ShipAdmin)
admin.site.register(Reimbursement, ReimbursementAdmin)
admin.site.register(Payout, PayoutAdmin)
