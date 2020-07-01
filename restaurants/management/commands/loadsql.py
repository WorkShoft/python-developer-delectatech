import ijson

from tqdm import tqdm
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from restaurants.models import Segment, Restaurant


class Command(BaseCommand):
    help = 'Load segment and restaurant data from restaurant and segment inputs'

    def add_arguments(self, parser):
         parser.add_argument('restaurant_json', nargs='+', type=str)
         parser.add_argument('segment_json', nargs='+', type=str)

    def handle(self, *args, **options):        
        with open(options['restaurant_json'][0], 'r') as restaurant_json, open(options['segment_json'][0], 'r') as segment_json:
            try:
                self.load_restaurants(restaurant_json)
                self.load_segments(segment_json)
                
            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(e))

    def load_restaurants(self, restaurant_json):
        """
        Clear and load restaurants
        """

        Restaurant.objects.all().delete()
        data = set(Restaurant(**i) for i in ijson.items(restaurant_json, "item"))
        Restaurant.objects.bulk_create(data)
        self.stdout.write(self.style.SUCCESS(f"Loaded {len(data)} restaurants"))        

        
    def load_segments(self, segment_json):
        """
        Clear and load segments
        """
        
        Segment.objects.all().delete()
        DYNAMIC_FIELDS = ('size', 'restaurants')

        segment_data = [
            {
                k:v for k, v in i.items() if k not in DYNAMIC_FIELDS
            } for i in ijson.items(segment_json, "item")
        ]

        segment_json.seek(0) # process the file again
        segment_restaurant_data = (set(i) for i in ijson.items(segment_json, "item.restaurants"))

        segment_objects = [Segment(**i) for i in segment_data]
        Segment.objects.bulk_create(segment_objects)
        self.stdout.write(self.style.SUCCESS(f"Loaded {len(segment_objects)} segments"))

        self.stdout.write(self.style.MIGRATE_HEADING(f"Creating segments - restaurants relationships..."))                
        with tqdm(total=len(segment_data)) as progress_bar:
            for index, uid_set in enumerate(segment_restaurant_data):
                segment_restaurant_objects = Restaurant.objects.filter(uidentifier__in=uid_set)
                segment_objects[index].restaurants.add(*segment_restaurant_objects)
                segment_objects[index].save()
                progress_bar.update(1)

