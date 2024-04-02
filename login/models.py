from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import RegexValidator


class Person(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    age = models.PositiveIntegerField() 

    mobile_number = models.CharField(
        max_length=15,
        validators=[
        RegexValidator(
            regex=r'^\d{10,15}$',
            message='Mobile number must be between 10 and 15 digits long.',
            code='invalid_mobile_number'
            )
        ]   
    )

    address = models.CharField(max_length=255)
    cities = [
      ("Mumbai", "Mumbai"),("Delhi","Delhi"),( "Bangalore", "Bangalore"),("Hyderabad","Hyderabad"),
      ("Ahmedabad","Ahmedabad"),("Chennai","Chennai"),("Kolkata","Kolkata"),("Surat","Surat"),
      ("Pune","Pune"),("Jaipur","Jaipur"),("Nadiad","Nadiad")
    ]
    city =models.CharField(max_length=10, choices=cities )
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
    class Meta:
        db_table ='doctor'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.is_staff = True
            
            super(Doctor, self).save(*args, **kwargs)
            
            doctor_group, created = Group.objects.get_or_create(name='Doctor')
            self.groups.add(doctor_group)
                    
        else:
            super(Doctor, self).save(*args, **kwargs)


