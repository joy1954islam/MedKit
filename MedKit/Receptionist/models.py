from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('Category',max_length=30)

    def __str__(self):
        return self.name


class Degree(models.Model):
    degree = models.CharField('Degree',max_length=10)

    def __str__(self):
        return self.degree