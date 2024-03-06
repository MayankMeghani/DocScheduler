# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person

class PersonCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username', 'email', 'address', 'mobile_number', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
