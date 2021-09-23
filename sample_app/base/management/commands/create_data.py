import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from base.models import Country, Disease, Dog, Infection, Vaccine, VaccineResearch

class Command(BaseCommand):
    help = 'Create db initial data'

    def handle(self, *args, **options):
        admin_user = User.objects.filter(username='admin').first()
        if not admin_user:
            admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'adm')

        country = Country.objects.create(name='Country')

        dogs = []
        for i in range(10):
            dog = Dog.objects.create(
                name    = f'Dog {i}',
                age     = i,
                owner   = admin_user)
            dogs.append(dog)

        vaccines = []
        for i in range(5):
            vaccine = Vaccine.objects.create(
                name                    = f'Vaccine {i}',
                manufacturer_country    = country)
            vaccines.append(vaccine)

            vaccine_researches = []
            for _ in range(100):
                vaccine_researches.append(
                    VaccineResearch(vaccine=vaccine, effectiveness=random.choice([0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])))
            VaccineResearch.objects.bulk_create(vaccine_researches)

        diseases = []
        for i in range(3):
            disease = Disease.objects.create(
                name            = f'Disease {i}',
                origin_country  = country)
            diseases.append(disease)

            infections = []
            for _ in range(100):
                infections.append(
                    Infection(disease=disease, lethal=random.choice([False, True, True, True, True, True])))
            Infection.objects.bulk_create(infections)

        # m2m fields

        for dog in dogs:
            other_dogs = [d for d in dogs if d != dog]
            dog.dog_friends.add(*other_dogs)

        for dog in dogs:
            dog.vaccines.add(*vaccines)

        for vaccine in vaccines:
            vaccine.covered_diseases.add(*diseases)

