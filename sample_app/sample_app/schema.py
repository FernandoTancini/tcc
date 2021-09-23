import graphene
from base.models import Disease, Dog, Vaccine
from django.contrib.auth.models import User
from django.db.models import Value
from django.db.models.fields import BooleanField
# from graphene.relay import Node
from graphene_django.debug import DjangoDebug
# from graphene_django.fields import DjangoConnectionField
# from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.schema import DjangoSchema
from graphene_django.types import DjangoObjectType
    

class DogType(DjangoObjectType):
    class Meta:
        model = Dog
        fields = ['name', 'age', 'dog_friends', 'vaccines']


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['owned_dogs']


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
    user = graphene.Field(UserType)

    def resolve_user(root, info):
        return info.context.user


schema = DjangoSchema(query=Query, automatic_preparation=True)
