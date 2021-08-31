from django.db import models
from django.db.models import deletion


class Dog(models.Model):
    class Meta:
        verbose_name = 'dog'
        verbose_name_plural = 'dogs'

    name = models.CharField('name', max_length=255)
    age = models.PositiveSmallIntegerField('age')
    dog_friends = models.ManyToManyField('base.Dog', verbose_name='dog friends')
    owner = models.ForeignKey('auth.User', deletion.CASCADE, verbose_name='owner', related_name='owned_dogs')


class Vaccine(models.Model):
    class Meta:
        verbose_name = 'vaccine'
        verbose_name_plural = 'vaccines'

    name = models.CharField('name', max_length=255)
    covered_diseases = models.ManyToManyField('base.Disease', verbose_name='dog friends')


class Disease(models.Model):
    class Meta:
        verbose_name = 'disease'
        verbose_name_plural = 'diseases'

    name = models.CharField('name', max_length=255)

