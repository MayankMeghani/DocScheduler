# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person,Patient,Doctor

class PersonCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username', 'email', 'address', 'mobile_number','is_staff','gender', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PatientCreationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['username', 'email', 'address', 'mobile_number', 'gender', 'blood_group','password']

# class PatientCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Patient
#         fields = ['username', 'email', 'password1', 'password2', 'address', 'mobile_number', 'gender', 'blood_group']
        
        
class DoctorCreationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['username', 'email', 'address', 'mobile_number', 'gender', 'specialization','password']
