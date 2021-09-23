from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from base.models import Disease, Dog, Vaccine

class Command(BaseCommand):
    help = 'Create db initial data'

    def handle(self, *args, **options):
        admin_user = User.objects.filter(username='admin').first()
        if not admin_user:
            admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'adm')

        dogs = []
        for i in range(10):
            dog = Dog.objects.create(
                name = f'Dog {i}',
                age = i,
                owner = admin_user)
            dogs.append(dog)

        vaccines = []
        for i in range(10):
            vaccine = Vaccine.objects.create(
                name = f'Vaccine {i}')
            vaccines.append(vaccine)

        diseases = []
        for i in range(10):
            disease = Disease.objects.create(
                name = f'Disease {i}')
            diseases.append(disease)

        # m2m fields

        for dog in dogs:
            other_dogs = [d for d in dogs if d != dog]
            dog.dog_friends.add(*other_dogs)

        for dog in dogs:
            dog.vaccines.add(*vaccines)

        for vaccine in vaccines:
            vaccine.covered_diseases.add(*diseases)

