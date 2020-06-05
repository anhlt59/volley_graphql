from django.core.management import BaseCommand, CommandError
from league.models import TeamSeason, Season, Team
from faker import Faker
from itertools import islice
import random


class Command(BaseCommand):
    help = "fake data"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help="number of records")

    def create_bulk_data(self, n):
        fake = Faker(["en-US"])
        seasons = list(Season.objects.all())
        teams = list(Team.objects.all())

        for _ in range(n):
            season = random.choice(seasons)
            team = random.choice(teams)
            name = ' '.join(fake.words())
            yield TeamSeason(season=season, name=name, team=team)

    def handle(self, *args, **options):
        N = options["number"]
        count = 0

        objs = self.create_bulk_data(N)

        while batch := list(islice(objs, 100)): # batch size = 100
            TeamSeason.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)
            self.stdout.write(f"Bulk created {count} TeamSeason")

        # collect stats
        total = TeamSeason.objects.count()
        self.stdout.write(f"\nTotal: {total}")
