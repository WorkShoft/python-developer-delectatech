from django.db import models


class Segment(models.Model):
    uidentifier = models.UUIDField(primary_key=True)
    
    name = models.TextField()
    average_popularity_rate = models.FloatField(null=True)
    average_satisfaction_rate = models.FloatField(null=True)
    average_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_reviews = models.IntegerField(null=True)

    @property
    def size(self):
        return len(self.restaurants.all())

    def __str__(self):
        return self.name

    def as_dict(self, extra_fields=False):
        if extra_fields:
            return {
                "name": self.name,
                "size": self.size,
                "uidentifier": str(self.uidentifier),
                "restaurants": [
                    r.as_dict() for r in self.restaurants.all()                    
                ],
                "average_popularity_rate": self.average_popularity_rate,
                "average_satisfaction_rate": self.average_satisfaction_rate,
                "average_price": self.average_price,
                "total_reviews": self.total_reviews,
            }
            
        return {
            "name": self.name,
            "size": self.size,
            "uidentifier": str(self.uidentifier),
            "restaurants": [
                r.as_dict() for r in self.restaurants.all()                    
            ],                
        }


class Restaurant(models.Model):
    uidentifier = models.UUIDField(primary_key=True)
    
    name = models.TextField()
    street_address = models.TextField(null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models. DecimalField(max_digits=10, decimal_places=7)
    city_name = models.TextField()
    popularity_rate = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    satisfaction_rate = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    total_reviews = models.IntegerField(null=True)
    average_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    segments = models.ManyToManyField(Segment, related_name="restaurants")
    
    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            "name": self.name,
            "street_address": self.street_address,
            "latitude": float(self.latitude) if self.latitude else None,
            "longitude": float(self.longitude) if self.longitude else None,
            "city_name": self.city_name,
            "popularity_rate": float(self.popularity_rate) if self.popularity_rate else None,
            "satisfaction_rate": float(self.satisfaction_rate) if self.satisfaction_rate else None,
            "total_reviews": int(self.total_reviews) if self.total_reviews else None,
            "uidentifier": str(self.uidentifier),
            "average_price": float(self.average_price) if self.average_price else None,
        }


