from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()
from accounts.forms import UserUpdateForm
from .forms import TakeAppointmentForm
from .models import Appointment


def PatientProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('PatientProfile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'Patient/PatientProfile.html', context)


def add_take_appointment(request,pk):
    person = get_object_or_404(Appointment, doctor=pk)
    form = TakeAppointmentForm(instance=person)
    if request.method == 'POST':
        form = TakeAppointmentForm(request.POST or None,instance=person)
        if form.is_valid():
            form.instance.patient = request.user
            form.save()
            return redirect('list_take_appointment')
    return render(request, 'Patient/Appointment/appointment_create.html', {'form': form})


def list_take_appointment(request):
    appointment = Appointment.objects.all()
    return render(request,'Patient/Appointment/appointment_list.html', {'appointment': appointment})