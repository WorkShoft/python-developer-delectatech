from django.db import models


class Segment(models.Model):
    uidentifier = models.UUIDField(primary_key=True)
    
    name = models.TextField()
    average_popularity_rate = models.FloatField(null=True)
    average_satisfaction_rate = models.FloatField(null=True)
    average_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_reviews = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    @property
    def size(self):
        return len(self.restaurants.all())

    
class Restaurant(models.Model):
    uidentifier = models.UUIDField(primary_key=True)
    
    name = models.TextField()
    street_address = models.TextField(null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models. DecimalField(max_digits=10, decimal_places=7)
    city_name = models.TextField()
    popularity_rate = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    satisfaction_rate = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    total_reviews = models.IntegerField()
    average_price = models.DecimalField(max_digits=10, decimal_places=2)

    segments = models.ManyToManyField(Segment, related_name="restaurants")
    
    def __str__(self):
        return self.name


