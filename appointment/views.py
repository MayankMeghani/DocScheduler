from django.shortcuts import render
from django.shortcuts import render ,redirect
from .models import Appointment
from login.models import Doctor,Patient
from .forms import AppointmentForm

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request,'doctor_list.html',{'doctors': doctors})

def book_appointment(request):
    if request.method == 'GET':
        patient_username = request.session.get('username')
        doctor_username = request.GET.get('doctor_username')
        print(patient_username, doctor_username)
        initial_data = {
            'patient_username': patient_username,
            'doctor_username': doctor_username,
        }
        form = AppointmentForm(initial=initial_data)
    else:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient_username = Patient.objects.get(username=request.session.get('username'))
            appointment.doctor_username = Doctor.objects.get(username=request.GET.get('doctor_username'))
            appointment.save()
            return redirect('/home_patient')

    return render(request, 'book_appointment.html', {'form': form})