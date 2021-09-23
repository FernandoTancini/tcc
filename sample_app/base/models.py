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
    vaccines = models.ManyToManyField('base.Vaccine', verbose_name='vacinas')

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Vaccine(models.Model):
    class Meta:
        verbose_name = 'vaccine'
        verbose_name_plural = 'vaccines'

    name = models.CharField('name', max_length=255)
    covered_diseases = models.ManyToManyField('base.Disease', verbose_name='dog friends')
    manufacturer_country = models.ForeignKey('base.Country', deletion.SET_NULL, null=True, verbose_name='manufacturer country', related_name='+')

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Disease(models.Model):
    class Meta:
        verbose_name = 'disease'
        verbose_name_plural = 'diseases'

    name = models.CharField('name', max_length=255)
    origin_country = models.ForeignKey('base.Country', deletion.SET_NULL, null=True, verbose_name='origin country', related_name='+')

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Country(models.Model):
    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    name = models.CharField('name', max_length=255)

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Infection(models.Model):
    class Meta:
        verbose_name = 'infection'
        verbose_name_plural = 'infections'

    lethal = models.BooleanField('lethal')
    disease = models.ForeignKey('base.Disease', deletion.CASCADE, verbose_name='disease', related_name='infections')


class VaccineResearch(models.Model):
    class Meta:
        verbose_name = 'vaccine research'
        verbose_name_plural = 'vaccine researches'

    effectiveness = models.DecimalField('effectiveness', decimal_places=4, max_digits=5)
    vaccine = models.ForeignKey('base.Vaccine', deletion.CASCADE, verbose_name='VACCINE', related_name='researches')
