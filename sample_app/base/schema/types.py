from base.models import Disease, Dog, Vaccine
from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['owned_dogs']
    

class DogType(DjangoObjectType):
    class Meta:
        model = Dog
        fields = ['name', 'age', 'dog_friends']


class VaccineType(DjangoObjectType):
    class Meta:
        model = Vaccine
        fields = ['name', 'covered_diseases']


class DiseaseType(DjangoObjectType):
    class Meta:
        model = Disease
        fields = ['name']
