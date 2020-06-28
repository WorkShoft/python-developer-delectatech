from django.db.models.fields import Field

from .models import Restaurant
from .custom_lookups import NotEqual


Field.register_lookup(NotEqual)    
    

class RestaurantRepo:
    model = Restaurant

    def _query(self, params={}, first=False):
        """
        Supports one condition per field
        Supports None values

        params: dict 
            {
                "popularity_rate": {"gt": 5.5},
                "satisfaction_rate": {"ne": None},
            }

        first : bool, optional
            Whether you want to retrieve one or many objects
        """
        
        filter_kwargs = {}
        exclude_kwargs = {}
        query = []
        
        for p in params:
            for operator, value in params[p].items():
                if value is not None:
                    filter_kwargs[f"{p}__{operator}"] = value
                else:
                    exclude_kwargs[f"{p}__isnull"] = True


        query = self.model.objects.filter(**filter_kwargs)

        query = query.exclude(**exclude_kwargs) if exclude_kwargs else query

        return query[0] if first else query
    
    def query_restaurants_first(self, params={}):
        """
        Query a single restaurant
        """
        
        return self._query(params=params, first=True)
    
    def query_restaurants(self, params={}):
        """
        Query a list of restaurants
        """
        
        return self._query(params=params)

