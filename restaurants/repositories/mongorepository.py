from .baserepository import BaseRepo
from restaurants.services import get_mongo_client


class MongoRestaurantRepo(BaseRepo):
    client = get_mongo_client()
    db = client.python_developer_db
    collection = db.segment_collection

    def _query(self, params={}, first=False, **kwargs):
        """
        Supports one condition per field
        Supports None values
        Duplicates need to be removed when many records are retrieved,
        because a restaurant can be embedded in several segments

        params: dict 
            {
                "popularity_rate": {"gt": 5.5},
                "satisfaction_rate": {"ne": None},
            }

        first : bool, optional
            Whether you want to retrieve one or many objects
        """

        params = {
            field: {f"${operator}": value for operator, value in condition.items()}
            for field, condition in params.items()
        }

        projection = {
            "_id": 0,
            "restaurants": {
                "$elemMatch": {
                    "$and": [{field: condition} for field, condition in params.items()]
                }
            },
        }

        query = [
            i["restaurants"][0]
            for i in self.collection.find({}, projection=projection)
            if i.get("restaurants")
        ]

        if first:
            return query[0]

        query_without_duplicates = [dict(i) for i in {tuple(q.items()) for q in query}]

        return query_without_duplicates
