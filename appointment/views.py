from django.shortcuts import render
from django.shortcuts import render ,redirect
from .models import Appointment
from login.models import Doctor,Patient
from .forms import AppointmentForm
from datetime import datetime,timedelta
from django.contrib import messages

def doctor_list(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as patient first.')
        return redirect('login')
    doctors = Doctor.objects.all()
    return render(request,'doctor_list.html',{'doctors': doctors})

def book_appointment(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as patient first.')
        return redirect('login')
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

def appointment_list(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as doctor first.')
        return redirect('login')
    doctor_username = request.session.get('username')
    tomorrow = datetime.now().date()+timedelta(days=1)
    appointments = Appointment.objects.filter(doctor_username__username=doctor_username, date__gte=tomorrow)
    return render(request, 'appointment_list.html', {'appointments': appointments})


def update_appointment_status(request, appointment_id):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as doctor first.')
        return redirect('login')
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        status = request.POST['status']
        appointment.status = status
        appointment.save()
        return redirect('/appointment_list')


def past_appointment_list(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as doctor first.')
        return redirect('login')
    doctor_username = request.session.get('username')
    today = datetime.now().date()
    
    past_appointments = Appointment.objects.filter(
        doctor_username__username=doctor_username,
        date__lt=today
    )
    
    today_appointments = Appointment.objects.filter(
        doctor_username__username=doctor_username,
        date=today,
        status__in=['Pending', 'Cancelled'] 
    )
    
    all_appointments = list(past_appointments) + list(today_appointments)
    
    return render(request, 'appointment_record.html', {'appointments': all_appointments})

def booked_appointment_list(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as patient first.')
        return redirect('login')
    current_username = request.session.get('username')
    
    current_user = Patient.objects.get(username=current_username)
    
    appointments = Appointment.objects.filter(patient_username=current_user)
    
    return render(request, 'booked_appointment.html', {'appointments': appointments})

