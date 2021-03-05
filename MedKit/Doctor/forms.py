from .models import *
from django import forms
from Patient.models import Appointment


class DoctorTestForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['test']


class UpdateDoctorTestForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['test']


class DoctorPrescribeForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['prescribe']


class UpdateDoctorPrescribeForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['prescribe']
