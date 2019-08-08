import datetime
from django.db import model


class appointment(models.Model):
    hospital_name=models.CharField(max_length=30)
    doctor_name=models.CharField(max_length=20)
    time=models.datetime()