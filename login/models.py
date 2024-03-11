from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models

class Person(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    name =models.CharField(max_length=30)
    age = models.PositiveIntegerField() 
    address = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDERS)
    class Meta:
        db_table ='person'

class Patient(Person):
    blood_group_choices=[
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ]
    blood_group = models.CharField(max_length=3,choices=blood_group_choices)
    class Meta:
        db_table ='patient'

class Doctor(Person):
    experience = models.PositiveIntegerField() 
    specialization = models.CharField(max_length=30)
    rating = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table ='doctor'

    def save(self, *args, **kwargs):
        self.is_staff = True
        super(Doctor, self).save(*args, **kwargs)