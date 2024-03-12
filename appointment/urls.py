from django.urls import path
from appointment import views

urlpatterns = [
    path('home_patient/doctor_list', views.doctor_list, name='home/patient/doctor_list'),
    path('home_patient/book_appointment', views.book_appointment, name='book_appointment'),
]