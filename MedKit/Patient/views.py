from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserUpdateForm


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
