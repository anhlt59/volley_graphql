from django.db import models
from django_extensions.db.models import TimeStampedModel, AutoSlugField


class Player(TimeStampedModel):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name} ({self.location})"