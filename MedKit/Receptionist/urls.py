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

    path('category/list/', views.list_category, name='list_category'),
    path('category/create/', views.create_category, name='create_category'),
    path('category/update/<int:pk>/', views.update_category, name='update_category'),
    path('category/delete/<int:pk>/', views.delete_category.as_view(), name='delete_category'),

    path('degree/list/', views.list_degree, name='list_degree'),
    path('degree/create/', views.create_degree, name='create_degree'),
    path('degree/update/<int:pk>/', views.update_degree, name='update_degree'),
    path('degree/delete/<int:pk>/', views.delete_degree.as_view(), name='delete_degree'),


    path('patient/', views.patient_list, name='patient_list'),
    path('appointment/list/', views.list_take_appointment, name='receptionist_list_take_appointment'),
    path('appointment/list/update/<int:pk>/', views.update_take_appointment, name='update_take_appointment'),
    path('appointment/list/view/<int:pk>/', views.view_take_appointment, name='view_take_appointment'),

    path('payment/list/', views.list_take_appointment_payment, name='list_take_appointment_payment'),

]
