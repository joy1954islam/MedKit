from django import forms

from .models import Appointment


class TakeAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['Number', 'TrxID', 'amount']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_apply = True
        user.save()
        return user
