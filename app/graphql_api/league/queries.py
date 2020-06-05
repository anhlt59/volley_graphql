import graphene
from graphene import relay
import graphql_jwt
from graphql_jwt.decorators import login_required
from graphene_django.filter import DjangoFilterConnectionField

from .types import (
    LeagueNode,
    SeasonNode,
    TeamNode,
    TeamSeasonNode,
    PlayerNode,
    PlayerInTeamNode,
    MatchNode,
)


class Query(graphene.ObjectType):
    all_leagues = DjangoFilterConnectionField(LeagueNode)
    league = relay.Node.Field(LeagueNode)

    # all_movies = graphene.List(MovieType)
    # movie = graphene.Field(MovieType, id=graphene.Int(), title=graphene.String())
    # all_movies = DjangoFilterConnectionField(MovieNode)
    # movie = relay.Node.Field(MovieNode)
    # all_directors = graphene.List(DirectorType)

    # @login_required
    # def resolve_all_movies(self, info, **kwargs):
    #     # user = info.context.user
    #     # if not user.is_authenticated:
    #     #     raise Exception("Auth credentials were not provided")
    #     return Movie.objects.all()

    # def resolve_all_directors(self, info, **kwargs):
    #     return Director.objects.all()

    # def resolve_movie(self, info, **kwargs):
    #     query_string = ""
    #
    #     for key, value in kwargs.items():
    #         if value:
    #             query_string += f"{key}={value},"
    #
    #     try:
    #         movie = eval(f"Movie.objects.get({query_string})")
    #     except Movie.DoesNotExist:
    #         movie = None
    #
    #     return movie