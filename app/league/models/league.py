from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel, AutoSlugField


class League(TimeStampedModel):
    name = models.CharField(
        max_length=100,
    )
    slug = AutoSlugField(
        populate_from=["name",],
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.name} ({self.owner})"