from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from .models import Category,Degree
from Patient.models import Appointment
User = get_user_model()


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ['degree']


class DoctorForm(UserCreationForm):

    # degree = forms.ModelMultipleChoiceField(
    #     queryset=Degree.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True

        user.save()

        return user

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))

        return email


class DoctorSignUpUpdateForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    degree = forms.ModelMultipleChoiceField(
        queryset=Degree.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'category', 'degree',]


class UpdateAppointmentForm(forms.ModelForm):
    date = forms.DateField(label='Date', widget=forms.SelectDateWidget)

    class Meta:
        model = Appointment
        fields = ['payment_status','meet_link','date','time']