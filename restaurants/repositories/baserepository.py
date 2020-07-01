class BaseRepo:
    def _query(self, params={}, first=False, as_dict=False):
        raise NotImplementedError

    def query_restaurants_first(self, params={}, as_dict=False):
        """
        Query a single restaurant
        """

        return self._query(params=params, first=True, as_dict=as_dict)

    def query_restaurants(self, params={}, as_dict=False):
        """
        Query a list of restaurants
        """

        return self._query(params=params, as_dict=as_dict)
