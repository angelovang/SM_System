from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms

UserModel = get_user_model()


class RegisterEmplForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel

        fields = ('username', 'email','password1', 'password2', 'first_name', 'last_name', 'phone_number')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username:', 'class': 'info'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email:', 'class': 'info'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Password:', 'class': 'info'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirm Password:', 'class': 'info'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name:', 'class': 'info'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name:', 'class': 'info'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number:', 'class': 'info'}),
        }

        labels = {
            'username': 'Username:',
            'email': 'Email:',
            'password1': 'Enter password:',
            'password2': 'Confirm password:',
            'first_name': 'First_name:',
            'last_name': 'Last_name:',
            'phone_number': 'Phone number'
        }

        help_texts = {
            'username': ('Required min 8 characters ( A-Z,a-z,0-9, @/./+/-/_ only )'),
            'password2':'Enter the same password !',
        }

# class LoginForm(auth_forms.AuthenticationForm):
#     class Meta:
#         model = UserModel
#
#         fields = ('username', 'password1')
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'Username:', 'class': 'info','autocomplete':'off'}),
#             'password1': forms.TextInput(attrs={'placeholder': 'Password:', 'class': 'info', 'autocomplete':'off'}),
#         }
#
#         labels = {
#             'username': 'Username:',
#             'password1': 'Enter password:',
#         }
