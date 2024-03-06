from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person

class PersonAdmin(UserAdmin):
    list_display = ('username', 'email', 'address', 'mobile_number', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'address', 'mobile_number')

admin.site.register(Person, PersonAdmin)
