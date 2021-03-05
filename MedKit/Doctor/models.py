from django.db import models
from django.conf import settings


# class Prescribe(models.Model):
#     doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pDoctors')
#     patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pPatients')
#     prescribe = models.TextField()
#
#     def __str__(self):
#         return self.prescribe
#
#
# class Test(models.Model):
#     doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tDoctors')
#     patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tPatients')
#     test = models.TextField()
#
#     def __str__(self):
#         return self.test
