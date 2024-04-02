from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person, Patient, Doctor
class PersonAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'age', 'mobile_number', 'address', 'city', 'gender')

admin.site.register(Person, PersonAdmin)
    

class PatientAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'age', 'mobile_number', 'address', 'city', 'gender', 'blood_group')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'profile_picture', 'age', 'mobile_number', 'address', 'city', 'gender','blood_group')}),
    )
admin.site.register(Patient, PatientAdmin)
    
class DoctorAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'age', 'mobile_number', 'address', 'city', 'gender', 'experience', 'specialization')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'profile_picture', 'age', 'mobile_number', 'address', 'city', 'gender','experience','specialization')}),
    )
admin.site.register(Doctor, DoctorAdmin)
