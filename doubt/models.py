from django.db import models
from login.models import Patient, Doctor

class Doubt(models.Model):
    patient_username = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.CharField( max_length=500)
    subject = models.CharField( max_length=50)
    STATUS_CHOICES = [
        ('solved', 'solved'),
        ('unsolved', 'unsolved'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unsolved')
    class Meta:
        db_table = 'Doubt'
    
    def get_STATUS_CHOICES(self):
        return self.STATUS_CHOICES

class Solution(models.Model):
    doubt = models.ForeignKey(Doubt, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'Solution'

    def __str__(self):
        return f"Solution for Doubt: {self.doubt.subject}"

    
