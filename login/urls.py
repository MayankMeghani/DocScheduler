from django.urls import path
from login import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_patient/', views.register_patient , name='register/patient'),
    path('register_doctor/', views.register_doctor , name='register/doctor'),
    path('login/', views.user_login, name='login'),
    path('', views.home, name='home'),
    path('home_doctor', views.home_doctor, name='home/doctor'),
    path('home_patient/', views.home_patient, name='home/patient'),
    path("logout/", views.logout_request, name="logout"),
]
