import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from league.models import (
    League,
    Season,
    Team,
    TeamSeason,
    Player,
    PlayerInTeam,
    Match,
)


class LeagueNode(DjangoObjectType):

    class Meta:
        model = League
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith',],
            # 'owner': ['exact', 'icontains', 'istartswith',],
        }
        interfaces = (relay.Node,)


class SeasonNode(DjangoObjectType):

    class Meta:
        model = Season
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith',],
            'league': ['exact',],
        }
        interfaces = (relay.Node,)


class TeamNode(DjangoObjectType):

    class Meta:
        model = Team
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith',],
            'location': ['exact'],
        }
        interfaces = (relay.Node,)


class TeamSeasonNode(DjangoObjectType):

    class Meta:
        model = TeamSeason
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith',],
            'team': ['exact'],
            'season': ['exact'],
        }
        interfaces = (relay.Node,)


class PlayerNode(DjangoObjectType):

    class Meta:
        model = Player
        filter_fields = {
            'first_name': ['exact', 'icontains', 'istartswith',],
            'last_name': ['exact', 'icontains', 'istartswith',],
        }
        interfaces = (relay.Node,)


class PlayerInTeamNode(DjangoObjectType):

    class Meta:
        model = PlayerInTeam
        filter_fields = {
            'player': ['exact'],
            'team': ['exact'],
        }
        interfaces = (relay.Node,)


class MatchNode(DjangoObjectType):

    class Meta:
        model = Match
        filter_fields = {
            'host': ['exact', 'icontains', 'istartswith',],
            'guest': ['exact', 'icontains', 'istartswith',],
        }
        interfaces = (relay.Node,)