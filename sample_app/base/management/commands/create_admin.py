from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create default admin user'

    def handle(self, *args, **options):
        print('Creating superuser...')
        if User.objects.filter(username='admin').exists():
            print('Already created!')
            return

        User.objects.create_superuser('admin', 'admin@example.com', 'adm')
        print('Successfully created!')
