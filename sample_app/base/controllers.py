from django.db.models import Count
from django.db.models.aggregates import Avg
from django.db.models.expressions import F, OuterRef, Subquery
from django.db.models.fields import FloatField
from django.db.models.functions import Cast

from base.models import Infection, VaccineResearch


def annotate_effectiveness(queryset):
    avg_effectiveness = VaccineResearch.objects \
        .filter(vaccine=OuterRef('pk')) \
        .values('vaccine') \
        .annotate(avg=Avg('effectiveness')) \
        .values('avg') \

    return queryset.annotate(effectiveness=Subquery(avg_effectiveness))
    

def annotate_lethality(queryset):
    infections_sq = Infection.objects.filter(disease=OuterRef('pk'))
    all_infection_count = infections_sq \
        .values('disease') \
        .annotate(count=Count('pk')) \
        .values('count')
    lethal_infection_count = infections_sq \
        .filter(lethal=True) \
        .values('disease') \
        .annotate(count=Count('pk')) \
        .values('count')
    queryset = queryset \
        .annotate(all_infection_count=Subquery(all_infection_count)) \
        .annotate(lethal_infection_count=Subquery(lethal_infection_count)) \
        .annotate(lethality=
            Cast(F('lethal_infection_count'), FloatField()) / Cast(F('all_infection_count'), FloatField()))
    
    return queryset
