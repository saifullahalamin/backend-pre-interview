from django.db import models


class Element(models.Model):
    data = models.ForeignKey('data.Data', on_delete=models.CASCADE, related_name='elements')
    device = models.ForeignKey('devices.Device', on_delete=models.CASCADE, related_name='elements')
    value = models.DecimalField(max_digits=19, decimal_places=5)
    record_time = models.DateTimeField()

    def __str__(self):
        return f"{self.data} {self.device} {self.value} {self.device.unit}"
