import os
import ijson

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure 

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Load segment collection from restaurant and segment inputs'

    def add_arguments(self, parser):
         parser.add_argument('restaurant_json', nargs='+', type=str)
         parser.add_argument('segment_json', nargs='+', type=str)

    def handle(self, *args, **options):        
        with open(options['restaurant_json'][0], 'r') as restaurant_json, open(options['segment_json'][0], 'r') as segment_json:
            try:
                client = self.get_mongo_client()
                db = client.python_developer_db                
                segment_collection = db.segment_collection

                # Reset collection and insert segments
                segment_collection.drop()
                segment_data = self.generator_from_json(segment_json)
                segment_collection.insert_many([i for i in segment_data])

                # Embed restaurants in their segments                
                inserted_restaurants = 0
                
                for segment in segment_collection.find():  
                    segment_restaurant_uids = set(segment["restaurants"])  
                    restaurant_data = self.generator_from_json(restaurant_json)

                    # Create a set with the restaurants that belong to this segment
                    uids = set(r["uidentifier"] for r in restaurant_data).intersection(segment_restaurant_uids)                     

                    restaurant_data = self.generator_from_json(restaurant_json)                    
                    insert_list = [r for r in restaurant_data if r["uidentifier"] in uids]

                    segment_name = segment["name"]
                    size = len(insert_list)
                    inserted_restaurants += size
                    print(f"{segment_name} -- {size} restaurants")
                    
                    segment_collection.update_one(
                        {
                            "_id": segment["_id"],
                        }, {
                                "$set": {"restaurants": insert_list},
                            }
                    )

                self.stdout.write(self.style.SUCCESS(f"Embedded {inserted_restaurants} restaurants in {segment_collection.count()} segments"))
                    
            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(e))

    def generator_from_json(self, json):
        json.seek(0) 
        return (i for i in ijson.items(json, "item", use_float=True))

    def get_mongo_client(self):
        try:
            CLIENT_TIMEOUT_SECONDS = 3
            MONGO_USERNAME = os.environ.get("MONGO_INITDB_ROOT_USERNAME") 
            MONGO_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD") 
            client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongo:27017", serverSelectionTimeoutMS=CLIENT_TIMEOUT_SECONDS)
            return client
        except ConnectionFailure as e:
            self.stdout.write(self.style.ERROR(e))
