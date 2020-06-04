from django.db import models
from django_extensions.db.models import TimeStampedModel, AutoSlugField


class Team(TimeStampedModel):
    name = models.CharField(
        max_length=100,
    )
    slug = AutoSlugField(
        populate_from=["name",],
    )
    location = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.location})"


class TeamSeason(TimeStampedModel):
    season = models.ForeignKey(
        "league.Season",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        "league.Team",#"Team"
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=100,
    )
    slug = AutoSlugField(
        populate_from=["name",],
    )

    def __str__(self):
        return f"{self.name} ({self.team} {self.session})"