from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person,Patient,Doctor

class PersonAdmin(UserAdmin):
    list_display = ('username','profile_picture', 'email', 'age', 'address','city', 'mobile_number', 'is_staff', 'is_active','gender')
    search_fields = ('username', 'email', 'address','city', 'mobile_number')
admin.site.register(Person, PersonAdmin)


class PatientAdmin(UserAdmin):
    list_display = ('username','profile_picture', 'email', 'age', 'address','city', 'mobile_number','gender','blood_group')
    search_fields = ('username', 'email', 'address', 'mobile_number')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'profile_picture', 'email', 'age', 'address','city', 'mobile_number', 'gender', 'blood_group','password1', 'password2'),
        }),
    )
admin.site.register(Patient,PatientAdmin)

class DoctorAdmin(UserAdmin):
    list_display = ('username','profile_picture', 'email', 'age', 'address','city', 'mobile_number','gender', 'experience','specialization','rating')
    search_fields = ('username', 'email','address', 'mobile_number')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'profile_picture', 'email', 'age','city', 'address', 'mobile_number', 'gender', 'specialization','password1', 'password2'),
        }),
    )
admin.site.register(Doctor,DoctorAdmin)
