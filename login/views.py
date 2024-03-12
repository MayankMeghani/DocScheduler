from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import PersonCreationForm, LoginForm,PatientCreationForm,DoctorCreationForm
from .models import Doctor
from django.core.exceptions import ValidationError

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorCreationForm(request.POST, request.FILES)
        if form.is_valid():
            age = form.cleaned_data['age']
            experience = form.cleaned_data['experience']
            if experience > age:
                raise ValidationError("Experience cannot be greater than age.")
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
            return redirect('/login')  
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
                request.session['is_staff'] = False
                if(user.is_staff==True):
                    request.session['is_staff'] = True
                    return redirect('/home_doctor')
                else:
                    return redirect('/home_patient') 
            else:
                return render(request, 'login.html', {'form': form})
    
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def home_doctor(request):
    return render(request, 'home_doctor.html')

def home_patient(request):
    return render(request, 'home_patient.html')

def logout_request(request):
    logout(request)
    if 'username' in request.session:
        del request.session['username']  # Clear username from session upon logout
    return redirect('/')


