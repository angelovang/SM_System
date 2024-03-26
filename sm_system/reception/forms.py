from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from sm_system.clients.models import Client
from sm_system.reception.models import ServiceOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = ['accept_date','client','device_type','device_data','issue_description','status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['accept_date'].widget.attrs['class'] = 'info'
        self.fields['accept_date'].widget = AdminDateWidget()
        self.fields['accept_date'].widget.attrs['date_format']= "%d %b, %Y"
        self.fields['client'].widget.attrs['class'] = 'info'
        self.fields['device_type'].widget.attrs['class'] = 'info'
        self.fields['device_data'].widget.attrs['class'] = 'info'
        self.fields['device_data'].widget.attrs['placeholder'] = 'Enter Producer,Model, Serial number and complectacion !'
        self.fields['issue_description'].widget.attrs['class'] = 'info'
        self.fields['status'].widget.attrs['class'] = 'info'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'info'
        self.fields['first_name'].widget.attrs['class'] = 'info'
        self.fields['last_name'].widget.attrs['class'] = 'info'
        self.fields['phone_number'].widget.attrs['class'] = 'info'