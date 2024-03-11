from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ( 'patient_username', 'doctor_username', 'time_slot', 'date', 'status')
    search_fields = ('patient_username', 'doctor_username')

admin.site.register(Appointment, AppointmentAdmin)