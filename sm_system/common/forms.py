from django import forms

from sm_system.common.models import ServiceInfo


class PostForm(forms.ModelForm):
    class Meta:
        model = ServiceInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['device'].widget.attrs['class'] = 'info'
        self.fields['description'].widget.attrs['class'] = 'info'
        self.fields['price'].widget.attrs['class'] = 'info'
