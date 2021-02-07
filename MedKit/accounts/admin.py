from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email','is_staff','is_doctor','is_patient',)


admin.site.register(User,UserAdmin)