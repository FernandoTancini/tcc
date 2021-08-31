import graphene

from graphene_django.debug import DjangoDebug

from base.schema import types as base_types
from graphql_jwt.decorators import login_required


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")
    profile = graphene.Field(base_types.UserType)

    def resolve_profile():
        pass




schema = graphene.Schema(query=Query)
