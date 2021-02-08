
from django.urls import path

from Patient import views

urlpatterns = [
    path('PatientProfile/',views.PatientProfile, name='PatientProfile'),
    path('appointment/<int:pk>/',views.add_take_appointment,name='add_take_appointment'),
    path('appointment/list/',views.list_take_appointment,name='list_take_appointment'),

    ]