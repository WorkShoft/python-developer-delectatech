import ijson
import os

from tqdm import tqdm

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure 


def generator_from_json(f):
    f.seek(0) 
    return (i for i in ijson.items(f, "item", use_float=True))

def get_mongo_client():
    try:
        CLIENT_TIMEOUT_SECONDS = 3
        MONGO_USERNAME = os.environ.get("MONGO_INITDB_ROOT_USERNAME") 
        MONGO_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD") 
        client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongo:27017", serverSelectionTimeoutMS=CLIENT_TIMEOUT_SECONDS)
        return client
    
    except ConnectionFailure as e:
        self.stdout.write(self.style.ERROR(e))

def embed_restaurant_data(segment_collection, restaurant_json, command=None):
    """
    Embed restaurants by intersecting restaurant and segment uids
    segment_collection: mongodb segment collection
    restaurant_json: list of restaurant objects in JSON format
    command (optional): BaseCommand. if set a success message will be printed using the command's styles
    """

    segment_count = segment_collection.count()
    inserted_restaurants = 0

    with tqdm(total=segment_count) as progress_bar:        
        for segment in segment_collection.find():  
            segment_restaurant_uids = set(segment["restaurants"])  
            restaurant_data = generator_from_json(restaurant_json)

            uids = set(r["uidentifier"] for r in restaurant_data).intersection(segment_restaurant_uids)                     
            restaurant_data = generator_from_json(restaurant_json)                    
            insert_list = [r for r in restaurant_data if r["uidentifier"] in uids]

            segment_name = segment["name"]
            size = len(insert_list)
            inserted_restaurants += size

            segment_collection.update_one(
                {
                    "_id": segment["_id"],
                }, {
                        "$set": {"restaurants": insert_list},
                    }
            )

            progress_bar.update(1)

    if command:
        command.stdout.write(command.style.SUCCESS(f"Embedded {inserted_restaurants} restaurant objects"))
