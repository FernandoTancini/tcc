from base.models import

class Command(BaseCommand):
    help = 'Create default admin user'

    def handle(self, *args, **options):
        print('Creating superuser...')
        if User.objects.filter(username='admin').exists():
            print('Already created!')
            return

        User.objects.create_superuser('admin', 'admin@example.com', 'adm')
        print('Successfully created!')
