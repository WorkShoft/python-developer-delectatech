from django.db.models.fields import Field

from .baserepository import BaseRepo
from restaurants.models import Restaurant
from restaurants.custom_lookups import NotEqual



Field.register_lookup(NotEqual)    
    

class SqlRestaurantRepo(BaseRepo):
    model = Restaurant

    def _query(self, params={}, first=False, as_dict=False):
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
        as_dict : bool, optional
            Whether you want to display the results in dict form
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
        query = [query[0]] if first else query
        query = [i.as_dict() for i in query] if as_dict else query
        
        return query[0] if first else query
    
