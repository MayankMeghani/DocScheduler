from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person,Patient,Doctor

class PersonAdmin(UserAdmin):
    list_display = ('username', 'email', 'address', 'mobile_number', 'is_staff', 'is_active','gender')
    search_fields = ('username', 'email', 'address', 'mobile_number')
admin.site.register(Person, PersonAdmin)


class PatientAdmin(UserAdmin):
    list_display = ('username', 'email', 'address', 'mobile_number','gender','blood_group')
    search_fields = ('username', 'email', 'address', 'mobile_number')
admin.site.register(Patient,PatientAdmin)

class DoctorAdmin(UserAdmin):
    list_display = ('username', 'email', 'address', 'mobile_number','gender','specialization','rating')
    search_fields = ('username', 'email', 'address', 'mobile_number')
admin.site.register(Doctor,DoctorAdmin)
