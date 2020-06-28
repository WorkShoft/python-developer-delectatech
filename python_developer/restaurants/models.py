from django.db import models


class Segment(models.Model):
    uidentifier = models.UUIDField(primary_key=True)
    
    name = models.TextField()
    size = models.IntegerField()
    average_popularity_rate = models.FloatField(null=True)
    average_satisfaction_rate = models.FloatField(null=True)
    average_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    
class Restaurant(models.Model):
    uidentifier = models.UUIDField(primary_key=True)
    
    name = models.TextField()
    street_address = models.TextField()
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models. DecimalField(max_digits=10, decimal_places=7)
    city_name = models.TextField()
    popularity_rate = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    satisfaction_rate = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    total_reviews = models.IntegerField()
    average_price = models.DecimalField(max_digits=10, decimal_places=2)

    segments = models.ManyToManyField(Segment)
    
    def __str__(self):
        return self.name


