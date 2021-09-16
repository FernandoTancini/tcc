import graphene
from base.models import Disease, Dog, Vaccine
from django.contrib.auth.models import User
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
        # return UserType.prepare(info.context.user, info.field_nodes[0], info)
        return info.context.user

        # users_qs = User.objects.all().prefetch_related('owned_dogs__dog_friends__vaccines__covered_diseases')
        # return users_qs.get(pk=info.context.user.pk)


schema = graphene.Schema(query=Query)
