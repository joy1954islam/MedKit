from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserUpdateForm


def DoctorProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
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