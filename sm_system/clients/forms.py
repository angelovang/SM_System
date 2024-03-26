from django import forms
from sm_system.clients.models import Client


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