from django.contrib import admin

# Register your models here.
from .models import Category,Degree

admin.site.register(Category)
admin.site.register(Degree)