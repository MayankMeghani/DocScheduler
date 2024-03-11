from django.db import models

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from login.models import Patient, Doctor


def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("Appointment date cannot be in the past.")


class Appointment(models.Model):
    patient_username = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_username = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    TIME_SLOTS=[
        ('Morning' , 'Morning'),
        ('AfterNoon' ,'AfterNoon'),
        ('evening' ,'evening'),
    ]
    time_slot = models.CharField(max_length=20,choices=TIME_SLOTS)
    # date = models.DateField(validators=[validate_future_date])
    date=models.CharField(max_length=20)
    STATUS_CHOICES = [
        ('Cancelled', 'Cancelled'),
        ('Confirmed', 'Confirmed'),
        ('Pending', 'Pending'),
    ]
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='Pending')
    class Meta:
        db_table = 'Appointment'
    