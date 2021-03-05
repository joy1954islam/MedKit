from django.shortcuts import render, get_object_or_404

from .forms import TakeAppointmentForm
from .models import Appointment
from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import UserUpdateForm
from django.contrib.auth import get_user_model
User = get_user_model()


def PatientProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('PatientProfile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'Patient/PatientProfile.html', context=context)


def add_take_appointment(request, pk):
    currentUser = request.user
    person = User.objects.get(pk=pk)
    form = TakeAppointmentForm()
    if request.method == 'POST':
        form = TakeAppointmentForm(request.POST or None)
        if form.is_valid():
            tk = form.save(commit=False)
            tk.doctor = person
            tk.patient = currentUser
            tk.save()
            return redirect('list_take_appointment')
    return render(request, 'Patient/Appointment/appointment_create.html', {'form': form})


def list_take_appointment(request):
    appointment = Appointment.objects.all()
    context = {
        'appointment': appointment
    }
    return render(request, 'Patient/Appointment/appointment_list.html', context=context)


def view_patient_prescribe(request, id):
    prescribe = Appointment.objects.filter(id=id)
    context = {
        'prescribe': prescribe
    }
    return render(request, 'Patient/view_prescribe.html', context=context)


def view_patient_test(request, id):
    test = Appointment.objects.filter(id=id)

    context = {
        'test': test
    }
    return render(request, 'Patient/view_test.html', context=context)