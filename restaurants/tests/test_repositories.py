from unittest.mock import MagicMock

from django.test import TestCase

from restaurants.models import Restaurant
from restaurants.repositories import sqlrepository, mongorepository
from restaurants.tests import fixtures


class TestRepositories(TestCase):
    def setUp(self):
        self.sqlrepo = sqlrepository.SqlRestaurantRepo()
        self.mongorepo = mongorepository.MongoRestaurantRepo()

        self.sqlrepo.query_restaurants_first = MagicMock(
            return_value=fixtures.SINGLE_QUERY_RESULT
        )
        self.sqlrepo.query_restaurants = MagicMock(
            return_value=fixtures.MANY_QUERY_RESULT
        )
        self.mongorepo.query_restaurants_first = MagicMock(
            return_value=fixtures.SINGLE_QUERY_RESULT
        )
        self.mongorepo.query_restaurants = MagicMock(
            return_value=fixtures.MANY_QUERY_RESULT
        )
        mongorepository.MongoRestaurantRepo.collection.find = MagicMock(
            return_value=[{"restaurants": fixtures.MANY_QUERY_RESULT,}]
        )

    def test_sqlrepo_query_restaurants_first(self):
        result = self.sqlrepo.query_restaurants_first()
        self.assertEqual(result, fixtures.SINGLE_QUERY_RESULT)

    def test_sqlrepo_query_restaurants(self):
        result = self.sqlrepo.query_restaurants()
        self.assertEqual(result, fixtures.MANY_QUERY_RESULT)

    def test_sqlrepo_query_internal(self):
        restaurant_object = Restaurant(**fixtures.SINGLE_QUERY_RESULT)
        restaurant_object.save()
        result = self.sqlrepo._query(params=fixtures.PARAMS, first=True, as_dict=True)
        self.assertEqual(result, fixtures.SINGLE_QUERY_RESULT)

    def test_mongorepo_query_first(self):
        result = self.mongorepo.query_restaurants_first()
        self.assertEqual(result, fixtures.SINGLE_QUERY_RESULT)

    def test_mongorepo_query_restaurants(self):
        result = self.mongorepo.query_restaurants()
        self.assertEqual(result, fixtures.MANY_QUERY_RESULT)

    def test_mongorepo_query_internal(self):
        result = self.mongorepo._query(params=fixtures.PARAMS)

        self.assertEqual(
            result[0]["uidentifier"], fixtures.MANY_QUERY_RESULT[0]["uidentifier"]
        )
