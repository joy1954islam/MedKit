from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from .models import Category,Degree

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
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))

        return email


class DoctorSignUpUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]

