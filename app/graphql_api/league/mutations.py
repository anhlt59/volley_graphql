import graphene
from graphene import relay
import graphql_jwt
from graphql_relay import from_global_id
from .types import LeagueNode


class LeagueUpdateMutationRelay(relay.ClientIDMutation):

    class Input:
        name = graphene.String()
        owner = graphene.ID()
        id = graphene.ID(required=True)

    league = graphene.Field(LeagueNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        if id := kwargs.get('id', None):
            data = {}
            if name := kwargs.get('name', None):
                data['name'] = name
            if owner := kwargs.get('owner', None):
                data['owner'] = owner
            League.objects.get(pk=from_global_id(id)[1]).update(**data)
            status = True
        else:
            status = False
        return LeagueUpdateMutationRelay(status=status)


class LeagueCreateMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String()
        owner = graphene.ID()

    league = graphene.Field(LeagueNode)

    def mutate(self, info, **kwargs):
        if (name := kwargs.get("name", None)) and (owner := kwargs.get("owner", None)):
            league = League.objects.create(name=name, owner=owner)
            mutation = LeagueCreateMutation(league=league)
        else:
            mutation = None

        return mutation


class Mutation:
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()
    # # revoke_token = graphql_jwt.Revoke.Field()

    create_leage = LeagueCreateMutation.Field()
    update_leage = LeagueUpdateMutationRelay.Field()
    # update_movie_relay = MovieUpdateMutationRelay.Field()
    # delete_movie = MovieDeleteMutation.Field()