import ijson

from django.core.management.base import BaseCommand, CommandError
from restaurants.models import Restaurant
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Load restaurant data from a JSON file'

    def add_arguments(self, parser):
         parser.add_argument('json', nargs='+', type=str)

    def handle(self, *args, **kwargs):        
        with open(kwargs['json'][0], 'r') as f:
            try: 
                data = set(Restaurant(**i) for i in ijson.items(f, "item"))
                Restaurant.objects.bulk_create(data)
                self.stdout.write(self.style.SUCCESS(f"Processed {len(data)} restaurants"))

            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(e))
