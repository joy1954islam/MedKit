from django.db import models
from django.conf import settings


class Prescribe(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,)
    prescribe = models.TextField()

    def __str__(self):
        return self.prescribe


class Test(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    test = models.TextField()

    def __str__(self):
        return self.test