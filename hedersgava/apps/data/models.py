from django.db import models


class Data(models.Model):

    def __str__(self):
        return f"{self.id}"
