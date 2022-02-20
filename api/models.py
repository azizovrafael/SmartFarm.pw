from django.db import models


class Arduino_Data(models.Model):
    w_temp = models.CharField(max_length=100, verbose_name='Weather Temperature', null=True, blank=True)
    w_humidity = models.CharField(max_length=100, verbose_name='Weather Humidity', null=True, blank=True)
    l_humidity_1 = models.CharField(max_length=100, verbose_name='Land Humidity 1', null=True, blank=True)
    l_humidity_2 = models.CharField(max_length=100, verbose_name='Land Humidity 2', null=True, blank=True)

