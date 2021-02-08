from django.db import models
from django.conf import settings


class Appointment(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                               related_name='doctor')
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='patient')
    Number = models.CharField(max_length=15,null=True,blank=True)
    TrxID = models.CharField(max_length=35,null=True,blank=True)
    amount = models.FloatField(max_length=10,null=True,blank=True)
    is_apply = models.BooleanField(default=False,null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.doctor)