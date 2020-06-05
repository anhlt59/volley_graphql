from django.core.management import BaseCommand, CommandError
from django.utils.timezone import get_current_timezone
from league.models import Match, TeamSeason
from faker import Faker
from itertools import islice
import random


class Command(BaseCommand):
    help = "fake data"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help="number of records")

    def create_bulk_data(self, n):
        SCORE_CHOICES = (1, 2, 3, 4, 5, 6)
        fake = Faker(["en-US"])
        teamseasons = list(TeamSeason.objects.all())

        for _ in range(n):
            host = random.choice(teamseasons)
            guest = random.choice(teamseasons)
            score = random.choice(SCORE_CHOICES)
            match_date = fake.date_time_this_year(tzinfo=get_current_timezone())
            yield Match(host=host, guest=guest, score=score, match_date=match_date)

    def handle(self, *args, **options):
        N = options["number"]
        count = 0

        objs = self.create_bulk_data(N)

        while batch := list(islice(objs, 100)): # batch size = 100
            Match.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)
            self.stdout.write(f"Bulk created {count} Match")

        # collect stats
        total = Match.objects.count()
        self.stdout.write(f"\nTotal: {total}")
