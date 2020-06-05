from django.core.management import BaseCommand, CommandError
from league.models import Season, League
from faker import Faker
from itertools import islice
import random


class Command(BaseCommand):
    help = "fake data"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help="number of records")

    def create_bulk_data(self, n):
        fake = Faker(["en-US"])
        leagues = list(League.objects.all())

        for _ in range(n):
            league = random.choice(leagues)
            name = ' '.join(fake.words())
            yield Season(name=name, league=league)

    def handle(self, *args, **options):
        N = options["number"]
        count = 0

        objs = self.create_bulk_data(N)

        while batch := list(islice(objs, 100)): # batch size = 100
            Season.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)
            self.stdout.write(f"Bulk created {count} Season")

        # collect stats
        total = Season.objects.count()
        self.stdout.write(f"\nTotal: {total}")
