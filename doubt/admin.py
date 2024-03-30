from django.contrib import admin
from .models import Doubt, Solution

# Register Doubt model
class DoubtAdmin(admin.ModelAdmin):
    list_display = ('subject', 'patient_username', 'status')
    list_filter = ('status',)
    search_fields = ('subject', 'description')

admin.site.register(Doubt, DoubtAdmin)

# Optionally, register Solution model if needed
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('doubt', 'doctor', 'description')
    search_fields = ('doubt__subject', 'description')

admin.site.register(Solution, SolutionAdmin)
