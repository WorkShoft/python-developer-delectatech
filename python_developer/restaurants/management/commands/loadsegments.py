import ijson

from django.core.management.base import BaseCommand, CommandError
from restaurants.models import Segment, Restaurant
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Load segment data from a JSON file'

    def add_arguments(self, parser):
         parser.add_argument('json', nargs='+', type=str)

    def handle(self, *args, **kwargs):        
        with open(kwargs['json'][0], 'r') as f:
            try:                
                segment_data = [{k:v for k, v in i.items() if k != 'restaurants'} for i in ijson.items(f, "item")]
                f.seek(0) # process the file again
                segment_restaurant_data = (i for i in ijson.items(f, "item.restaurants"))              

                segment_objects = [Segment(**i) for i in segment_data]
                Segment.objects.bulk_create(segment_objects)

                processed_restaurants = 0
                for index, uid in enumerate(segment_restaurant_data):
                    segment_restaurant_objects = Restaurant.objects.filter(uidentifier__in=uid)
                    segment_objects[index].restaurants.add(*segment_restaurant_objects)
                    segment_objects[index].save()
                    processed_restaurants += len(segment_restaurant_objects)

                self.stdout.write(self.style.SUCCESS(f"Processed {len(segment_data)} segments for a total of {processed_restaurants} restaurants"))

            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(e))
