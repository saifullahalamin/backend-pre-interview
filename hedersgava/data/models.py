from django.db import models


class Data(models.Model):
    record_time = models.DateTimeField()

    def __str__(self):
        return self.id
