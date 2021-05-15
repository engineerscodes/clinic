from django.db import models


class Details(models.Model):
    mobile = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.mobile


class Report(models.Model):
    patient = models.ForeignKey(Details, default=None,
                                on_delete=models.CASCADE, related_name='info', primary_key=True)
    message = models.TextField(default=None)

    # def __str__(self):
    #     return self.patient
