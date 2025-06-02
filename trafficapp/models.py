from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    SIGNAL_CHOICES = [
        ('red', 'Red'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
    ]
    signal_status = models.CharField(max_length=10, choices=SIGNAL_CHOICES, default='red')

    TRAFFIC_CHOICES = [
        ('clear', 'Clear'),
        ('congested', 'Congested'),
    ]
    traffic_condition = models.CharField(max_length=10, choices=TRAFFIC_CHOICES, default='clear')

    def __str__(self):
        return self.name

