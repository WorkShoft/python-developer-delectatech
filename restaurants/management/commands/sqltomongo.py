from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from restaurants import services
from restaurants.models import Segment


class Command(BaseCommand):
    help = "Migrate SQL data to MongoDB"

    def handle(self, *args, **kwargs):
        try:
            client = services.get_mongo_client()
            db = client.python_developer_db
            segment_collection = db.segment_collection

            self.stdout.write(self.style.MIGRATE_HEADING(f"Serializing SQL data..."))
            data = [s.as_dict(extra_fields=True) for s in Segment.objects.all()]

            # Clear collection and migrate data
            segment_collection.remove({})

            self.stdout.write(
                self.style.MIGRATE_HEADING(f"Inserting data into MongoDB...")
            )
            segment_collection.insert(data)

            # Output report
            segment_size = len(data)
            restaurant_size = sum([i["size"] for i in data])
            self.stdout.write(
                self.style.SUCCESS(
                    f"Migrated {segment_size} segments with {restaurant_size} restaurants"
                )
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
