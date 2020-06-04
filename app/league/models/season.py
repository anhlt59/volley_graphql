from django.db import models
from django_extensions.db.models import TimeStampedModel, AutoSlugField


class Season(TimeStampedModel):
    league = models.ForeignKey(
        "league.League",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=100,
    )
    slug = AutoSlugField(
        populate_from=["name"],
    )

    def __str__(self):
        return f"{self.name} ({self.league})"