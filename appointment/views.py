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
    # selected_city = request.GET.get('city')
    # if selected_city:
    #     doctors = Doctor.objects.filter(city=selected_city)
    # else:
    #     doctors = Doctor.objects.all()
    # return render(request, 'doctor_list.html', {'doctors': doctors})
    doctors = Doctor.objects.all()
    return render(request,'doctor_list.html',{'doctors': doctors})

def book_appointment(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as patient first.')
        return redirect('login')
    if request.method == 'POST' or "GET":
        patient_username = request.session.get('username')
        doctor_username = request.POST.get('doctor_username') or request.session.get('doctor_username')  
        print(patient_username,doctor_username)
        initial_data = {
            'patient_username': Patient.objects.get(username=patient_username),
            'doctor_username': Doctor.objects.get(username=doctor_username)
        }
        form = AppointmentForm(initial=initial_data)
        return render (request, 'book_appointment.html', {'form': form})



def processing_appointment(request):    
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as patient first.')
        return redirect('login')
    form = AppointmentForm(request.POST)
    if form.is_valid():
        appointment = form.save(commit=False)
        doctor_username = form.cleaned_data['doctor_username']
        patient_username = form.cleaned_data['patient_username']  
        time_slot = form.cleaned_data['time_slot']
        date = form.cleaned_data['date']
        # Check if a similar appointment already exists
        existing_appointment = Appointment.objects.filter(
            doctor_username__username=doctor_username,
            patient_username__username=patient_username,
            time_slot=time_slot,
            date=date,
            ).exists()

        if existing_appointment:
            messages.warning(request, 'This appointment already exists.')
            request.session["doctor_username"] = doctor_username.username
            return redirect(book_appointment)
        
        # No existing appointment found, save the new appointment

        appointment.patient_username = Patient.objects.get(username=patient_username)
        appointment.doctor_username = Doctor.objects.get(username=doctor_username)
        appointment.save()
        messages.warning(request, 'Appintment is succesfully booked.')
        return redirect('/home_patient')
    else:
        doctor_username = form.cleaned_data['doctor_username']
        request.session["doctor_username"] = doctor_username.username
        messages.warning(request, 'This Slot in not available for appoinment.')
        return redirect('book_appointment') 

def appointment_list(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as doctor first.')
        return redirect('login')
    doctor_username = request.session.get('username')
    tomorrow = datetime.now().date()+timedelta(days=1)
    appointments = Appointment.objects.filter(doctor_username__username=doctor_username, date__gte=tomorrow)
    for appointment in appointments:
        patient_username = appointment.patient_username
        patient = Patient.objects.get(username=patient_username)
        appointment.patient = patient
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
    for appointment in all_appointments:
        patient_username = appointment.patient_username
        patient = Patient.objects.get(username=patient_username)
        appointment.patient = patient
    return render(request, 'appointment_record.html', {'appointments': all_appointments})

def booked_appointment_list(request):
    if not request.user.is_authenticated :
        messages.warning(request, 'You need to log in as patient first.')
        return redirect('login')
    current_username = request.session.get('username')
    
    current_user = Patient.objects.get(username=current_username)
    
    appointments = Appointment.objects.filter(patient_username=current_user)
    for appointment in appointments:
        # Fetch the corresponding doctor object based on the username
        doctor_username = appointment.doctor_username
        doctor = Doctor.objects.get(username=doctor_username)
        # Assign the doctor object to a new attribute in the appointment
        appointment.doctor = doctor
    return render(request, 'booked_appointment.html', {'appointments': appointments})

