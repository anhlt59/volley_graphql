from django.core.management import BaseCommand, CommandError
from django.contrib.auth.models import User
from league.models import League
from faker import Faker
from itertools import islice
import random


class Command(BaseCommand):
    help = "fake data"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help="number of records")

    def create_bulk_data(self, n):
        fake = Faker(["en-US"])
        users = list(User.objects.all())

        for _ in range(n):
            owner = random.choice(users)
            name = ' '.join(fake.words())
            yield League(owner=owner, name=name)

    def handle(self, *args, **options):
        N = options["number"]
        count = 0

        objs = self.create_bulk_data(N)

        while batch := list(islice(objs, 100)): # batch size = 100
            League.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)
            self.stdout.write(f"Bulk created {count} League")

        # collect stats
        total = League.objects.count()
        self.stdout.write(f"\nTotal: {total}")
