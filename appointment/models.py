from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from login.models import Patient, Doctor
import datetime
today = datetime.date.today()


class Appointment(models.Model):
    patient_username = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_username = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    TIME_SLOTS=[
        ('Morning' , 'Morning'),
        ('AfterNoon' ,'AfterNoon'),
        ('evening' ,'evening'),
    ]
    time_slot = models.CharField(max_length=20,choices=TIME_SLOTS)

    past_7_days = [today - datetime.timedelta(days=i+1) for i in range(7)]
    next_7_days = [today + datetime.timedelta(days=i+1) for i in range(7)]
    DATE_CHOICES = tuple([(today, today.strftime('%d-%m-%Y'))] + [(d, d.strftime('%d-%m-%Y')) for d in past_7_days + next_7_days])
    date = models.DateField(max_length=20, choices=DATE_CHOICES)

    STATUS_CHOICES = [
        ('Cancelled', 'Cancelled'),
        ('Confirmed', 'Confirmed'),
        ('Pending', 'Pending'),
    ]
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='Pending')
    issue = models.CharField(max_length=500)
        
    # def clean(self):
    #     if Appointment.objects.filter(
    #         doctor_username=self.doctor_username,
    #         date=self.date,
    #         time_slot=self.time_slot
    #     ).count() >= 5:
    #         raise ValidationError("The doctor cannot have more than 5 appointments for the same time slot on the same day.")

    class Meta:
        db_table = 'Appointment'
    
    def get_STATUS_CHOICES(self):
        return self.STATUS_CHOICES
    
    