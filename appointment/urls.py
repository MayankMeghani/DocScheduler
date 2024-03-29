from django.urls import path
from appointment import views

urlpatterns = [
    path('home_patient/doctor_list', views.doctor_list, name='home/patient/doctor_list'),
    path('home_patient/book_appointment', views.book_appointment, name='book_appointment'),
    path('home_patient/processing_appointment', views.processing_appointment, name='processing_appointment'),
    path('appointment_list', views.appointment_list, name='appointment_list'),
    path('update_appointment_status/<int:appointment_id>/', views.update_appointment_status, name='update_appointment_status'),
    path('past_appointment_list', views.past_appointment_list, name='past_appointment_list'),
    path('home_patient/booked_appointment_list', views.booked_appointment_list, name='booked_appointment_list'),
]