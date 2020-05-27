from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_login, auth_logout
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
import math

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True, unique=True)
    location = models.CharField(max_length=40)
    DESIGNATION_CHOICES = (
        ('WI', 'Work Inspector'),
        ('JE', 'Junior Engineer'),
        ('DEE', 'Deputy Executive Engineer')
    )
    designation = models.CharField(max_length=4, choices=DESIGNATION_CHOICES)

    def __str__(self):
        return self.user.username

    USERNAME_FIELD = 'email'


class Reading(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Date = models.DateField()
    major = models.CharField(max_length=30, blank=False, null=False)
    front = models.FloatField(default=0, blank=True)
    rear_sill = models.FloatField(default=0, blank=True)
    vent = models.FloatField(default=0, blank=True)
    opening = models.FloatField(default=0, blank=True)
    driving_head = models.DecimalField(max_digits=15, decimal_places=6, blank=True, default=0)
    discharge = models.DecimalField(max_digits=15, decimal_places=6, blank=True, default=0)
    remarks = models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):

        self.driving_head = self.front - self.rear_sill
        self.discharge = 7 * self.vent * math.sqrt(self.driving_head) * self.opening
        super(Reading, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


