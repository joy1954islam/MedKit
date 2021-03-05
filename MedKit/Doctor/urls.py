

from django.urls import path

from .views import *

urlpatterns = [
    path('DoctorProfile/', DoctorProfile, name='DoctorProfile'),
    path('appointment/list/', list_take_appointment, name='doctor_list_take_appointment'),
    path('createTest/<int:patient_id>/', create_doctor_test, name='createTest'),
    path('view_doctor_test/<int:id>/', view_doctor_test, name='view_doctor_test'),
    path('create_doctor_prescribe/<int:patient_id>/', create_doctor_prescribe, name='create_doctor_prescribe'),
    path('update_doctor_test/<int:id>/', update_doctor_test, name='update_doctor_test'),
    path('update_doctor_prescribe/<int:id>/', update_doctor_prescribe, name='update_doctor_prescribe'),
    path('view_doctor_prescribe/<int:id>/', view_doctor_prescribe, name='view_doctor_prescribe'),



]
