from django.db import models


class StarshipModel(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)

    length = models.IntegerField()
    hyperdrive_rating = models.FloatField()
    cargo_capacity = models.IntegerField()

    crew = models.IntegerField()
    passengers = models.IntegerField()


class Starship(models.Model):
    name = models.CharField(max_length=255)
    model = models.ForeignKey(StarshipModel, related_name='ships')
    price = models.IntegerField()
