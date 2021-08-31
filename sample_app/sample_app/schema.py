import graphene
from base.models import Disease, Dog, Vaccine
from django.contrib.auth.models import User
from graphene_django.debug import DjangoDebug
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['owned_dogs']
    

class DogType(DjangoObjectType):
    class Meta:
        model = Dog
        fields = ['name', 'age', 'dog_friends', 'vaccines']


class VaccineType(DjangoObjectType):
    class Meta:
        model = Vaccine
        fields = ['name', 'covered_diseases']


class DiseaseType(DjangoObjectType):
    class Meta:
        model = Disease
        fields = ['name']


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")
    profile = graphene.Field(UserType)

    @login_required
    def resolve_profile(root, info):
        return info.context.user


schema = graphene.Schema(query=Query)
