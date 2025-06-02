from django.db import models

class Signal(models.Model):
    signalStatus = models.CharField(max_length=20)
    trafficCondition = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.signalStatus} - {self.trafficCondition}"







