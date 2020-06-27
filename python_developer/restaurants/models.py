from django.db import models


class Restaurant(models.Model):
    uidentifier = models.UUIDField(primary_key=True)
    
    name = models.TextField()
    street_address = models.TextField()
    location = models.PointField()
    city_name = models.TextField()
    popularity_rate = models.FloatField()
    satisfaction_rate = models.FloatField()
    total_reviews = models.IntegerField()
    average_price = models.FloatField()

    segments = models.ManyToManyField(Segment)
    
    @property
    def latitude(self):
        return self.location.x

    @property
    def longitude(self):
        return self.location.y

    def __str__(self):
        return self.name


class Segment(models.Model):
    uidentifier = models.UUIDField(primary_key=True)
    
    name = models.TextField()
    size = models.IntegerField()
    average_popularity_rate = models.FloatField(null=True)
    average_satisfaction_rate = models.FloatField(null=True)
    average_price = models.DecimalField(decimal_places=2)

    restaurants = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.name
