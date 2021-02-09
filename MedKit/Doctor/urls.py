

from django.urls import path

from Doctor import views

urlpatterns = [
        path('DoctorProfile/',views.DoctorProfile, name='DoctorProfile'),
        path('appointment/list/', views.list_take_appointment, name='doctor_list_take_appointment'),
    ]