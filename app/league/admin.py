from django.contrib import admin
from .models import (
    League,
    Season,
    Team,
    TeamSeason,
    Player,
    PlayerInTeam,
    Match,
)


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "created",
    )


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
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

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "height",
        "weight",
        "date_of_birth",
        "created",
    )


@admin.register(PlayerInTeam)
class PlayerInTeamAdmin(admin.ModelAdmin):
    list_display = (
        "player",
        "team",
        "created",
    )


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        "host",
        "guest",
        "match_date",
        "score",
    )