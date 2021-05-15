from django.db import models


class Details(models.Model):
    mobile = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
