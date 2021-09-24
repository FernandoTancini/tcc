import graphene
from base.controllers import annotate_effectiveness, annotate_lethality
from base.models import Country, Disease, Dog, Vaccine
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg
from graphene_django.debug import DjangoDebug
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
        fields = ['name', 'covered_diseases', 'manufacturer_country']

    effectiveness = graphene.Float()
    def annotate_effectiveness(root_qs, info):
        return annotate_effectiveness(root_qs)

    # def resolve_effectiveness(root, info):
    #     return root.researches.aggregate(avg=Avg('effectiveness'))['avg']


class DiseaseType(DjangoObjectType):
    class Meta:
        model = Disease
        fields = ['name', 'origin_country']

    lethality = graphene.Float()
    def annotate_lethality(root_qs, info):
        return annotate_lethality(root_qs)

    # def resolve_lethality(root, info):
    #     return root.infections.filter(lethal=True).count() / root.infections.all().count()



class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        fields = ['name']


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")
    user = graphene.Field(UserType)

    def resolve_user(root, info):
        return info.context.user


schema = DjangoSchema(query=Query, automatic_preparation=True)
# schema = DjangoSchema(query=Query)
