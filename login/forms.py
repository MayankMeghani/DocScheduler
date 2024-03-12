from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person,Patient,Doctor

class PersonCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username','profile_picture', 'email','name', 'age', 'address', 'mobile_number','is_staff','gender', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PatientCreationForm(PersonCreationForm):
    class Meta:
        model = Patient
        fields = ['username','profile_picture', 'email','name', 'age', 'address', 'mobile_number', 'gender', 'blood_group','password1','password2']
        
class DoctorCreationForm(PersonCreationForm):
    class Meta:
        model = Doctor
        fields = ['username','profile_picture', 'email', 'name', 'age','address', 'mobile_number', 'gender', 'experience', 'specialization','password1','password2']
