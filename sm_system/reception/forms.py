from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from sm_system.reception.models import ServiceOrder, OrdersHistory


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


class RepairStartForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = ['accept_date','client','device_data','issue_description','status','technician']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accept_date'].disabled = True
        self.fields['client'].disabled = True
        self.fields['device_data'].disabled = True
        self.fields['issue_description'].disabled = True
        self.fields['status'].disabled = True
        self.fields['technician'].disabled = True


class HistoryForm(forms.ModelForm):
    class Meta:
        model = OrdersHistory
        fields = '__all__'


