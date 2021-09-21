from graphene_django.schema import DjangoSchema
from django.db.models.fields import BooleanField
import graphene
from base.models import Disease, Dog, Vaccine
from django.contrib.auth.models import User
from django.db.models import Value
from graphene_django.debug import DjangoDebug
from graphene_django.types import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['owned_dogs']
    

class DogType(DjangoObjectType):
    class Meta:
        model = Dog
        fields = ['name', 'age', 'dog_friends', 'vaccines']

    is_pretty = graphene.Boolean()
    def annotate_is_pretty(qs, _info):
        return qs.annotate(is_pretty=Value(True, output_field=BooleanField()))

    is_prettyy = graphene.NonNull(graphene.List(graphene.NonNull(graphene.Boolean)))
    def resolve_is_prettyy(self, _info):
        return [True, False]


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

    def resolve_profile(root, info):
        return info.context.user


schema = DjangoSchema(query=Query)
