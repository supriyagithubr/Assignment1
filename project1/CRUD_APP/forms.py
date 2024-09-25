from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        labels = {
            'o_id' : 'ID',
            'name' : 'NAME',
            'organization' : 'ORGANIZATION',
            'city' : 'CITY',
            'phone_no': 'PHONE',
            'email' : 'EMAIL',
            'last_updated_date' : 'UPDATED_DATE',
            'status' : 'STATUS',
            # 'active': 'ACTIVE'

        }