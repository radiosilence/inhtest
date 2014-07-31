from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Backup the scaffold data from here to the remote backup server"

    def handle(self, *args, **options):
        u = User.objects.create(
            username='test',
            email='test@example.com',
            password=u'test',  # test
            is_superuser=True,
            is_staff=True
        )
        u.set_password('test')
        u.save()
