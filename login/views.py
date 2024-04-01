from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import PersonCreationForm, LoginForm,PatientCreationForm,DoctorCreationForm
from django.core.exceptions import ValidationError
from datetime import datetime
from appointment.models import Appointment
from django.contrib import messages
from .models import Patient,Person

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorCreationForm(request.POST, request.FILES)
        if form.is_valid():
            age = form.cleaned_data['age']
            experience = form.cleaned_data['experience']
            if experience > age:
                messages.error(request, "Experience cannot be greater than age.")
                form = DoctorCreationForm()
                return render(request, 'register_doctor.html', {'form': form})
            form.save()
            return redirect('/login')  
    else:
        form = DoctorCreationForm()
    return render(request, 'register_doctor.html', {'form': form})


def register_patient(request):
    if request.method == 'POST':
        form = PatientCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Registration successful." )
            return redirect('/login')
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = PatientCreationForm()
        return render(request, 'register_patient.html', {'form': form})
    else:
        form = PatientCreationForm()
    return render(request, 'register_patient.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = PersonCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  
    else:
        form = PersonCreationForm()
    return render(request, 'register.html', {'form': form})
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = user.username
                request.session['is_staff'] = user.is_staff
                if user.is_staff:
                    return redirect('/home_doctor')
                else:
                    return redirect('/home_patient')
            else: 
                if Person.objects.filter(username=username).exists():
                    messages.error(request, 'Incorrect password')
                else:
                    messages.error(request, 'Username does not exist')
        else:
            messages.error(request, 'Invalid form submission')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def home_doctor(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as doctor first.')
        return redirect('login')
    today = datetime.now().date()
    appointments = Appointment.objects.filter(
        doctor_username__username=request.session.get('username'),
        date=today,
        status="Confirmed"
    )
    for appointment in appointments:
        patient_username = appointment.patient_username
        patient = Patient.objects.get(username=patient_username)
        appointment.patient = patient
    return render(request, 'home_doctor.html', {'appointments': appointments})


def home_patient(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as patient first.')
        return redirect('login')
    return render(request, 'home_patient.html')


def logout_request(request):
    logout(request)
    if 'username' in request.session:
        del request.session['username'] 
    request.user = None    
    return redirect('/')


def user_profile(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in first.')
        return redirect('login')
    return render(request, 'user_profile.html')

