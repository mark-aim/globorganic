from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from authentication.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User;
        fields=('first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2');

        widgets={
            'first_name' : forms.TextInput(attrs={'placeholder':'First name'}),
            'last_name' : forms.TextInput(attrs={'placeholder':'Last name'}),
            'username' : forms.TextInput(attrs={'placeholder':'Choose a Username'}),
            'email' : forms.TextInput(attrs={'placeholder':'Email'}),
            'phone_number' : forms.TextInput(attrs={'placeholder':'Phone number'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': "Type a Password"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': "Confirm your Password"})


class CostumUserLoginForm(forms.ModelForm):
    password =  forms.CharField(label="password", widget=forms.PasswordInput);

    class Meta:
        model=User;
        fields=('username', 'password');

        widgets={
            'username' : forms.TextInput(attrs={'placeholder':'Choose a Username'}),
        }

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username'];
            password = self.cleaned_data['password']

            if not authenticate(username = username, password = password):
                raise forms.ValidationError('Invalid Username or Password.');

    def __init__(self, *args, **kwargs):
        super(CostumUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': "Type a Password"})