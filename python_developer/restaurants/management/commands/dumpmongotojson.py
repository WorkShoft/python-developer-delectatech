import json

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from restaurants import services


class Command(BaseCommand):
    help = 'Output a JSON with a Mongo segment collection, including embedded data'

    def add_arguments(self, parser):
         parser.add_argument('json', nargs='+', type=str)

    def handle(self, *args, **kwargs):        
        with open(kwargs['json'][0], 'w') as f:
            try:
                client = services.get_mongo_client()
                db = client.python_developer_db
                collection = db.segment_collection
                
                data = {
                    str(s["uidentifier"]): s
                    for s in collection.find({}, projection={"_id": False})
                }
                
                f.write(json.dumps(data))

                self.stdout.write(self.style.SUCCESS(f"Dumped {collection.count()} segments"))

            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(e))
