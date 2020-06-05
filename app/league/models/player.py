from django.db import models
from django_extensions.db.models import TimeStampedModel, AutoSlugField


class Player(TimeStampedModel):
    first_name = models.CharField(
        max_length=100,
    )
    last_name = models.CharField(
        max_length=100,
    )
    slug = AutoSlugField(
        populate_from=["first_name", "last_name"],
    )
    height = models.FloatField(
        help_text="In cm",
    )
    weight = models.FloatField(
        help_text="In kg",
    )
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class PlayerInTeam(TimeStampedModel):
    player = models.ForeignKey(
        "Player",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        "league.TeamSeason",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.player} ({self.team})"