# myapp/urls.py
from django.urls import path
from .views import register, user_login,home,logout_request,register_patient,register_doctor

urlpatterns = [
    path('register/', register, name='register'),
    path('register/patient/', register_patient , name='register/patient'),
    path('register/doctor/', register_doctor , name='register/doctor'),
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),
    path("logout/", logout_request, name="logout"),
]
