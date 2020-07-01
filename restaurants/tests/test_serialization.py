from django.test import TestCase

from restaurants.models import Segment, Restaurant
from restaurants.tests import fixtures


class TestSerialization(TestCase):
    def setUp(self):
        self.restaurant = Restaurant(**fixtures.SINGLE_QUERY_RESULT)
        self.restaurant.save()
        self.segment = Segment(**fixtures.VERY_SMALL_SEGMENT)
        self.segment.save()
        self.segment.restaurants.add(self.restaurant)
        self.segment.save()

    def test_restaurant_as_dict(self):
        restaurant_dict = self.restaurant.as_dict()
        self.assertEqual(restaurant_dict, fixtures.SINGLE_QUERY_RESULT)

    def test_segment_as_dict(self):
        segment_dict = self.segment.as_dict()
        restaurants_dict = {"restaurants": [self.restaurant.as_dict()]}
        embedded_dict = {**segment_dict, **restaurants_dict}

        self.assertEqual(embedded_dict, segment_dict)
