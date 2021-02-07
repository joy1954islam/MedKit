
from django.urls import path

from Patient import views

urlpatterns = [
        path('PatientProfile/',views.PatientProfile, name='PatientProfile'),

    ]