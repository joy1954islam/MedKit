from django.contrib import admin

# Register your models here.
from .models import Prescribe,Test

admin.site.register(Prescribe)
admin.site.register(Test)