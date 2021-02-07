from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.

from django.shortcuts import render
from accounts.forms import UserUpdateForm, ChangeEmailForm
from django.views.generic import View, FormView, DeleteView
from django.conf import settings
from django.utils.crypto import get_random_string
from accounts.models import Activation
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from accounts.utils import (
    send_activation_email, send_reset_password_email, send_forgotten_username_email, send_activation_change_email,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView, PasswordChangeView as BasePasswordChangeView,
    PasswordResetDoneView as BasePasswordResetDoneView, PasswordResetConfirmView as BasePasswordResetConfirmView,
)

from django.contrib.auth import get_user_model

from .forms import DoctorForm,DoctorSignUpUpdateForm,CategoryForm,DegreeForm
from .models import Category,Degree

User = get_user_model()


def SuperAdminHome(request):
    return render(request,'Receptionist/Home.html')


def SuperAdminProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('SuperAdminProfile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'Receptionist/Profile/SuperAdminProfile.html', context)


class ChangeEmailView(LoginRequiredMixin, FormView):
    template_name = 'Receptionist/Profile/change_email.html'
    form_class = ChangeEmailForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        user = self.request.user
        email = form.cleaned_data['email']

        if settings.ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE:
            code = get_random_string(20)

            act = Activation()
            act.code = code
            act.user = user
            act.email = email
            act.save()

            send_activation_change_email(self.request, email, code)

            messages.success(self.request, f'To complete the change of email address, click on the link sent to it.')
        else:
            user.email = email
            user.save()

            messages.success(self.request, f'Email successfully changed.')

        return redirect('SuperAdmin_change_email')


class ChangeEmailActivateView(View):
    @staticmethod
    def get(request, code):
        act = get_object_or_404(Activation, code=code)

        # Change the email
        user = act.user
        user.email = act.email
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(request, f'You have successfully changed your email!')

        return redirect('SuperAdmin_change_email')


class ChangePasswordView(BasePasswordChangeView):
    template_name = 'Receptionist/Profile/change_password.html'

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(self.request, f'Your password was changed.')

        return redirect('log_in')


class DoctorSignUpView(FormView):
    template_name = 'Receptionist/Doctor/partial_doctor_create.html'
    form_class = DoctorForm

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)

        if settings.DISABLE_USERNAME:
            # Set a temporary username
            user.username = get_random_string()
        else:
            user.username = form.cleaned_data['username']

        if settings.ENABLE_USER_ACTIVATION:
            user.is_active = False

        # Create a user record
        user.save()

        # Change the username to the "user_ID" form
        if settings.DISABLE_USERNAME:
            user.username = f'user_{user.id}'
            user.save()

        if settings.ENABLE_USER_ACTIVATION:
            code = get_random_string(20)

            act = Activation()
            act.code = code
            act.user = user
            act.save()

            send_activation_email(request,user.email, code)

            messages.success(request,f'Account is Created and You are signed up. To activate the account, follow the '
                                     f'link sent to the mail.')
        else:
            raw_password = form.cleaned_data['password1']

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,f'You are successfully signed up!')

        return redirect('doctor_list')


def doctor_list(request):
    employees = User.objects.all()
    # MyFilter = GovtUserFilter(request.GET,queryset=employees)
    # employees = MyFilter.qs
    context = {
        'employees': employees,
        # 'MyFilter':MyFilter,
    }
    return render(request, 'Receptionist/Doctor/doctor_list.html', context)


def doctor_update(request,pk):
    course = get_object_or_404(User, pk=pk)
    form = DoctorSignUpUpdateForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, "User Updated Successfully")
        return redirect("doctor_list")
    # else:
    #     messages.error(request, "Training Not Updated Successfully")
    return render(request, 'Receptionist/Doctor/partial_doctor_update.html', {'form': form})


def doctor_delete(request, pk):
    employee = get_object_or_404(User, pk=pk)
    data = dict()
    if request.method == 'POST':
        employee.delete()
        data['form_is_valid'] = True
        employees = User.objects.all()
        data['html_employee_list'] = render_to_string('Receptionist/Doctor/partial_doctor_list.html',
                                                      {'employees': employees })
    else:
        context = {'employee': employee}
        data['html_form'] = render_to_string('Receptionist/Doctor/partial_doctor_delete.html', context, request=request)
    return JsonResponse(data)


def doctor_view(request, pk):
    employee = get_object_or_404(User, pk=pk)
    data = dict()
    context = {'employee': employee}
    data['html_form'] = render_to_string('Receptionist/Doctor/partial_doctor_view.html', context, request=request)
    return JsonResponse(data)


def list_category(request):
    category = Category.objects.all()
    return render(request,'Receptionist/Category/category_list.html',{'category': category})


def create_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_category')
    return render(request, 'Receptionist/Category/category_create.html', {'form': form})


def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list_category')
    return render(request, 'Receptionist/Category/category_update.html', {'form': form})


class delete_category(DeleteView):
    model = Category
    template_name = 'Receptionist/Category//category_delete.html'
    success_url = 'http://127.0.0.1:8000/Receptionist/category/list/'


def list_degree(request):
    degree = Degree.objects.all()
    return render(request,'Receptionist/Degree/degree_list.html',{'degree': degree})


def create_degree(request):
    form = DegreeForm()
    if request.method == 'POST':
        form = DegreeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('list_degree')
    return render(request, 'Receptionist/Degree/degree_create.html', {'form': form})


def update_degree(request, pk):
    degree = get_object_or_404(Degree, pk=pk)
    form = DegreeForm(instance=degree)
    if request.method == 'POST':
        form = DegreeForm(request.POST, instance=degree)
        if form.is_valid():
            form.save()
            return redirect('list_degree')
    return render(request, 'Receptionist/Degree/degree_update.html', {'form': form})


class delete_degree(DeleteView):
    model = Degree
    template_name = 'Receptionist/Degree//degree_delete.html'
    success_url = 'http://127.0.0.1:8000/Receptionist/degree/list/'


def patient_list(request):
    patient = User.objects.all()
    # MyFilter = GovtUserFilter(request.GET,queryset=employees)
    # employees = MyFilter.qs
    context = {
        'patient': patient,
        # 'MyFilter':MyFilter,
    }
    return render(request, 'Receptionist/Patient/patient_list.html', context)

