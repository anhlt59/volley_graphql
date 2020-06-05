from django.core.management import BaseCommand, CommandError
from league.models import Player
from faker import Faker
from itertools import islice
import random


class Command(BaseCommand):
    help = "fake data"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help="number of records")

    def create_bulk_data(self, n):
        fake = Faker(["en-US"])

        for _ in range(n):
            first_name = fake.first_name()
            last_name = fake.last_name()
            height = random.choice(range(165, 200))
            if height < 170:
                weight = random.choice(range(55, 70))
            elif height < 180:
                weight = random.choice(range(65, 80))
            elif height < 190:
                weight = random.choice(range(75, 90))
            else:
                weight = random.choice(range(85, 100))
            date_of_birth = fake.date_of_birth(minimum_age=17, maximum_age=35)
            yield Player(first_name=first_name, last_name=last_name, height=height,
                         weight=weight, date_of_birth=date_of_birth)

    def handle(self, *args, **options):
        N = options["number"]
        count = 0

        objs = self.create_bulk_data(N)

        while batch := list(islice(objs, 100)): # batch size = 100
            Player.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)
            self.stdout.write(f"Bulk created {count} Player")

        # collect stats
        total = Player.objects.count()
        self.stdout.write(f"\nTotal: {total}")
