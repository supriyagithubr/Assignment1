from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['o_id', 'name', 'organization','city','phone_no', 'email','last_updated_date','status']
admin.site.register(Order, OrderAdmin)
