from django.core.management import BaseCommand, CommandError
from league.models import PlayerInTeam, Player, TeamSeason
from faker import Faker
from itertools import islice
import random


class Command(BaseCommand):
    help = "fake data"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help="number of records")

    def create_bulk_data(self, n):
        fake = Faker(["en-US"])
        players = list(Player.objects.all())
        teamseasons = list(TeamSeason.objects.all())

        for _ in range(n):
            player = random.choice(players)
            team = random.choice(teamseasons)
            yield PlayerInTeam(player=player, team=team)

    def handle(self, *args, **options):
        N = options["number"]
        count = 0

        objs = self.create_bulk_data(N)

        while batch := list(islice(objs, 100)): # batch size = 100
            PlayerInTeam.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)
            self.stdout.write(f"Bulk created {count} PlayerInTeam")

        # collect stats
        total = PlayerInTeam.objects.count()
        self.stdout.write(f"\nTotal: {total}")
