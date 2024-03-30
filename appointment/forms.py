from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor_username','patient_username','time_slot', 'date','issue']
        widgets = {
            'doctor_username': forms.HiddenInput(),
            'patient_username': forms.HiddenInput()
        }
    # def __init__(self, *args, **kwargs):
    #     super(AppointmentForm, self).__init__(*args, **kwargs)
    #     self.fields['doctor_username'].disabled = True
    #     self.fields['patient_username'].disabled = True