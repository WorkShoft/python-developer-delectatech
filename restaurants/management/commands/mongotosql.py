import warnings

from tqdm import tqdm

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from restaurants import services
from restaurants.models import Segment, Restaurant


class Command(BaseCommand):
    help = "Migrate MongoDB data to SQL"

    def handle(self, *args, **kwargs):
        try:
            client = services.get_mongo_client()
            db = client.python_developer_db
            collection = db.segment_collection

            self.stdout.write(self.style.MIGRATE_HEADING(f"Cleaning SQL tables..."))
            Segment.objects.all().delete()
            Restaurant.objects.all().delete()

            self.stdout.write(
                self.style.MIGRATE_HEADING(f"Deserializing MongoDB data...")
            )
            data = [s for s in collection.find({})]

            self.stdout.write(
                self.style.MIGRATE_HEADING(
                    f"Migrating data and creating relationships..."
                )
            )

            with tqdm(total=len(data)) as progress_bar:
                for segment in data:
                    segment_data = {
                        k: v
                        for k, v in segment.items()
                        if k not in ("restaurants", "size", "_id",)
                    }

                    # Create Segment objects
                    segment_object = Segment(**segment_data)
                    segment_object.save()
                    # Create Restaurant objects
                    restaurant_objects = set(
                        Restaurant(**r) for r in segment["restaurants"]
                    )

                    # bulk_create skips duplicates when ignore_conflicts is True
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        Restaurant.objects.bulk_create(
                            restaurant_objects, ignore_conflicts=True
                        )

                    # Create relationships
                    segment_object.restaurants.add(*restaurant_objects)
                    progress_bar.update(1)

        except IntegrityError as e:
            return False
