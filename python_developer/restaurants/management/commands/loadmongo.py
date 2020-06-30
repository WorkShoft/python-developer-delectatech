import ijson

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from restaurants import services


class Command(BaseCommand):
    help = 'Load segment collection from restaurant and segment inputs'

    def add_arguments(self, parser):
         parser.add_argument('restaurant_json', nargs='+', type=str)
         parser.add_argument('segment_json', nargs='+', type=str)

    def handle(self, *args, **options):        
        with open(options['restaurant_json'][0], 'r') as restaurant_json, open(options['segment_json'][0], 'r') as segment_json:
            try:
                client = services.get_mongo_client()
                db = client.python_developer_db                

                self.load_segments(segment_json, db)
                self.load_restaurants(restaurant_json, db)
                    
            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(e))


    def load_segments(self, segment_json, db):
        """ 
        Reset collection and insert segments
        """
        
        segment_collection = db.segment_collection

        # Reset collection and insert segments
        segment_collection.drop()
        segment_data = services.generator_from_json(segment_json)
        segment_collection.insert_many([i for i in segment_data])


    def load_restaurants(self, restaurant_json, db):
        """
        1) Clear current embedded data
        2) Intersect restaurant and segment uid data
        3) Embed restaurant data
        """

        segment_collection = db.segment_collection
        segment_count = segment_collection.count()
        
        self.stdout.write(self.style.MIGRATE_HEADING(f"Embedding restaurant data in {segment_count} segments..."))
    
        inserted_restaurants = services.embed_restaurant_data(segment_collection, restaurant_json, command=self)
