import json

from restaurants.models import Segment

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Output a JSON with segments, including its restaurants"

    def add_arguments(self, parser):
        parser.add_argument("json", nargs="+", type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs["json"][0], "w") as f:
            try:
                segment_data = Segment.objects.all()

                data = {str(s.uidentifier): s.as_dict() for s in segment_data}

                f.write(json.dumps(data))

                self.stdout.write(
                    self.style.SUCCESS(f"Dumped {len(segment_data)} segments")
                )

            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(e))
