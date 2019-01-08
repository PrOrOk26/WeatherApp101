from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateField()
    