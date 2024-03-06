# myapp/models.py
from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models

class Person(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)

class Patient(Person):
    blood_group = models.CharField(max_length=15, blank=True, null=True)
    

class Doctor(Person):
    specialization = models.CharField(max_length=30, blank=True, null=True)
    rating = models.IntegerField()