from django.urls import path

from Receptionist import views

urlpatterns = [
    path('ReceptionistHome/', views.SuperAdminHome, name='ReceptionistHome'),
    path('ReceptionistProfile/',views.SuperAdminProfile, name='SuperAdminProfile'),
    path('change/password/', views.ChangePasswordView.as_view(), name='SuperAdmin_change_password'),
    path('change/email/', views.ChangeEmailView.as_view(), name='SuperAdmin_change_email'),
    path('change/email/<code>/', views.ChangeEmailActivateView.as_view(), name='change_email_activation'),

    path('Doctor/', views.doctor_list, name='doctor_list'),
    path('doctor/create/', views.DoctorSignUpView.as_view(), name='doctor_create'),
    path('<int:pk>/doctor/update/', views.doctor_update, name='doctor_update'),
    path('<int:pk>/doctor/delete/', views.doctor_delete, name='doctor_delete'),
    path('<int:pk>/doctor/view/', views.doctor_view, name='doctor_view'),
]
