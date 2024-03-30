from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group
class Person(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    # name =models.CharField(max_length=30)
    age = models.PositiveIntegerField() 
    mobile_number = models.CharField(max_length=15)
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
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         # Set the group to "admin" for new Person instances
    #         group = Group.objects.get(name='Admin')
    #         self.groups.add(group)
    #     super(Person, self).save(*args, **kwargs)
    
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
        # if not self.pk:
            # Set the group to "doctor" for new Doctor instances
            # group = Group.objects.get(name='Doctors')
            # self.groups.add(group)
        super(Doctor, self).save(*args, **kwargs)