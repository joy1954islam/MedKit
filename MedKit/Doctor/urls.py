

from django.urls import path

from Doctor import views

urlpatterns = [
        path('DoctorProfile/',views.DoctorProfile, name='DoctorProfile'),

    ]