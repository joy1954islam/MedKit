
from django.urls import path

from .views import *

urlpatterns = [
    path('PatientProfile/', PatientProfile, name='PatientProfile'),
    path('appointment/<int:pk>/', add_take_appointment, name='add_take_appointment'),
    path('appointment/list/', list_take_appointment, name='list_take_appointment'),
    path('view_patient_test/<int:id>/', view_patient_test, name='view_patient_test'),
    path('view_patient_prescribe/<int:id>/', view_patient_prescribe, name='view_patient_prescribe'),

    ]