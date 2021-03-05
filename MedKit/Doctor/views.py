from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from accounts.forms import UserUpdateForm
from Patient.models import Appointment
from .forms import *
from django.contrib.auth import get_user_model
User = get_user_model()


def DoctorProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('DoctorProfile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'Doctor/DoctorProfile.html', context)


def list_take_appointment(request):
    appointment = Appointment.objects.all()
    context = {
        'appointment': appointment,
    }
    return render(request, 'Doctor/Appointment/appointment_list.html', context=context)


def create_doctor_test(request, patient_id):
    test = Appointment.objects.get(id=patient_id)
    if request.method == 'GET':
        form = DoctorTestForm()
        context = {
            'form': form
        }
        return render(request, 'Doctor/Test/test_create.html', context=context)

    if request.method == 'POST':
        form = DoctorTestForm(request.POST or None, instance=test)
        if form.is_valid():
            form.save()
            return redirect(reverse('doctor_list_take_appointment'))
    context = {
        'form': form
    }
    return render(request, 'Doctor/Test/test_create.html', context=context)


def view_doctor_test(request, id):
    test = Appointment.objects.filter(id=id)

    context = {
        'test': test
    }
    return render(request, 'Doctor/Test/test_view.html', context=context)


def update_doctor_test(request,id):
    appointment = get_object_or_404(Appointment, pk=id)
    form = UpdateDoctorTestForm(instance=appointment)
    if request.method == 'POST':
        form = UpdateDoctorTestForm(request.POST or None, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect(reverse('doctor_list_take_appointment'))
    context = {
        'form': form
       }
    return render(request, 'Doctor/Test/test_update.html', context=context)


def create_doctor_prescribe(request, patient_id):
    prescribe = Appointment.objects.get(id=patient_id)
    if request.method == 'GET':
        form = DoctorPrescribeForm()
        context = {
            'form': form
        }
        return render(request, 'Doctor/Prescribe/create_prescribe.html', context=context)

    if request.method == 'POST':
        form = DoctorPrescribeForm(request.POST or None, instance=prescribe)
        if form.is_valid():
            form.save()
            return redirect(reverse('doctor_list_take_appointment'))
    context = {
        'form': form
    }
    return render(request, 'Doctor/Prescribe/create_prescribe.html', context=context)


def view_doctor_prescribe(request, id):
    prescribe = Appointment.objects.filter(id=id)
    context = {
        'prescribe': prescribe
    }
    return render(request, 'Doctor/Prescribe/view_prescribe.html', context=context)


def update_doctor_prescribe(request,id):
    appointment = get_object_or_404(Appointment, pk=id)
    form = UpdateDoctorPrescribeForm(instance=appointment)
    if request.method == 'POST':
        form = UpdateDoctorPrescribeForm(request.POST or None, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect(reverse('doctor_list_take_appointment'))
    context = {
        'form': form
    }
    return render(request, 'Doctor/Prescribe/update_prescribe.html', context=context)
