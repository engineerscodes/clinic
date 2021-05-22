from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DOCTORS(models.Model):

    doctor = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return "EMAIL: "+self.doctor.email + " | USERNAME: "+self.doctor.username
