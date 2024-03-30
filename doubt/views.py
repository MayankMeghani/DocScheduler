from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doubt, Solution
from .forms import DoubtForm,SolutionForm
from login.models import Patient,Doctor

def doubt_list(request):
    doubts = Doubt.objects.all()
    return render(request, 'doubt/doubt_list.html', {'doubts': doubts})

def user_doubts(request):
    current_username = request.session.get('username')    
    current_user = Patient.objects.get(username=current_username)
    user_doubts = Doubt.objects.filter(patient_username=current_user)
    return render(request, 'doubt/asked_doubt.html', {'doubts': user_doubts})

def solved_doubts(request):
    doctor_username = request.session.get('username')
    doctor = Doctor.objects.get(username=doctor_username)
    solutions = Solution.objects.filter(doctor=doctor)
    # # solved_doubts = Doubt.objects.filter(doubt=doubt)
    # doubt_ids = [solution.doubt_id for solution in solutions]
    # solved_doubts = Doubt.objects.filter(id__in=doubt_ids)
    return render(request, 'doubt/solved_doubt.html',{'solutions':solutions})
    # return render(request, 'doubt/doubt_list.html',{'solutions':solutions})


def doubt_solution(request, doubt_id):
    doubt = get_object_or_404(Doubt, pk=doubt_id)
    solutions = Solution.objects.filter(doubt=doubt)
    return render(request, 'doubt/doubt_solution.html', {'doubt': doubt, 'solutions': solutions})

def doubt_create(request):
    if request.method == 'GET':
        patient_username = request.session.get('username')
        initial_data = {
            'patient_username': patient_username
        }
        form = DoubtForm(initial=initial_data)
    else:
        form = DoubtForm(request.POST)
        if form.is_valid():
            doubt = form.save(commit=False)
            doubt.patient_username = Patient.objects.get(username=request.session.get('username'))  # Assuming user is logged in
            doubt.save()
            return redirect('/home_patient/doubt')
    
    return render(request, 'doubt/doubt_create.html', {'form': form})

def create_solution(request, doubt_id):
    doubt = get_object_or_404(Doubt, pk=doubt_id)
    if not request.user.is_staff:  # Assuming is_staff is True for doctors
        messages.error(request, "Patients cannot add solutions.")
        return redirect('/doubt/list')
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.doubt = doubt
            doubt.status='solved'
            doubt.save()
            doctor_username = request.session.get('username')
            doctor = Doctor.objects.get(username=doctor_username)
            solution.doctor = doctor 
            solution.save()
            return redirect('/home_doctor/doubt', doubt_id=doubt_id)
    else:
        form = SolutionForm()
    return render(request, 'doubt/add_solution.html', {'form': form, 'doubt': doubt})

def update_solution(request, solution_id):
    solution = get_object_or_404(Solution, pk=solution_id)
    if request.method == 'POST':
        form = SolutionForm(request.POST, instance=solution)
        if form.is_valid():
            form.save()
            return redirect('/home_doctor/doubt')  # Redirect to solved doubts page after update
    else:
        form = SolutionForm(instance=solution)
    return render(request, 'doubt/add_solution.html', {'form': form, 'solution': solution})


def delete_solution(request, solution_id):
    solution = get_object_or_404(Solution, pk=solution_id)

    other_solutions_count = Solution.objects.filter(doubt=solution.doubt).exclude(id=solution_id).count()

    if other_solutions_count == 0:
        doubt = solution.doubt
        doubt.status = 'unsolved'
        doubt.save()
    solution.delete()
    return redirect('/home_doctor/doubt')

def update_doubt(request, doubt_id):
    doubt = get_object_or_404(Doubt, pk=doubt_id)
    if request.method == 'POST':
        form = DoubtForm(request.POST, instance=doubt)
        if form.is_valid():
            form.save()
            return redirect('/home_patient/doubt')
    else:
        form = DoubtForm(instance=doubt)
        patient_username = request.session.get('username')
        print(patient_username)
    return render(request, 'doubt/doubt_create.html', {'form': form, 'doubt': doubt ,'patient_username' : patient_username})


def delete_doubt(request, doubt_id):
    doubt = get_object_or_404(Doubt, pk=doubt_id)
    doubt.delete()
    return redirect('/home_patient/doubt')