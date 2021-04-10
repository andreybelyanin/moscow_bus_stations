from django.db import models


class Route(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Station(models.Model):

    name = models.CharField(max_length=200)
    routes = models.ManyToManyField(Route, verbose_name="Маршруты", related_name="stations")
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f'{self.name} {self.longitude} {self.latitude}'
