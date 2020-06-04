from django.contrib import admin
from .models import (
    League,
    Season,
    Team,
    TeamSeason,
)


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "created",
    )


@admin.register(Season)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "league",
        "created",
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "created",
    )


@admin.register(TeamSeason)
class TeamSeasonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "team",
        "season",
        "created",
    )

