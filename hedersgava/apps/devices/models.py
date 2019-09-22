from django.db import models


class Device(models.Model):
    code = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    unit = models.CharField(max_length=254, blank=True, null=True, default='')

    def __str__(self):
        return f"{self.code} {self.name}"
