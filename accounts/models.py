from django.db import models
from django.contrib.auth.models import AbstractUser


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام شهر")

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    city = models.ForeignKey(City, null=True, blank=False, on_delete=models.CASCADE)
