from django.db import models
from django.db.models.lookups import IntegerGreaterThanOrEqual

SEX_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "other"),
)


class Details(models.Model):
    mobile = models.CharField(max_length=50, primary_key=True,)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='male')
    age = models.PositiveIntegerField(default=18)
    saturation_level = models.FloatField(default=80)
    heart_rate = models.FloatField(default=130)
    is_checked = models.BooleanField(default=False)
    Form_date = models.DateField(default='2001-04-12')
    # verfiyed_by=models.EmailField()

    def __str__(self):
        return self.mobile


class Report(models.Model):
    patient = models.OneToOneField(
        Details, default=None, on_delete=models.CASCADE, related_name='info', to_field='mobile',
        primary_key=True)
    message = models.TextField(default=None)
    doctor_name = models.CharField(max_length=50)
    client_name = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.patient
