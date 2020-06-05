from django.core.management import BaseCommand, CommandError
from league.models import Team
from faker import Faker
from itertools import islice


class Command(BaseCommand):
    help = "fake data"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help="number of records")

    def create_bulk_data(self, n):
        fake = Faker(["en-US"])

        for _ in range(n):
            location = fake.location_on_land()[-1]
            name = ' '.join(fake.words())
            yield Team(location=location, name=name)

    def handle(self, *args, **options):
        N = options["number"]
        count = 0

        objs = self.create_bulk_data(N)

        while batch := list(islice(objs, 100)): # batch size = 100
            Team.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)
            self.stdout.write(f"Bulk created {count} Team")

        # collect stats
        total = Team.objects.count()
        self.stdout.write(f"\nTotal: {total}")
