from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Backup the scaffold data from here to the remote backup server"

    def handle(self, *args, **options):
        User.objects.create(
            username='test',
            email='test@example.com',
            password=u'pbkdf2_sha256$12000$rLnMaukpmTqb$vjOIjdSkG6VBApWzPVJO/1IXBWIkCs9duNJpVfQ5cDc=',  # hi
            is_superuser=True,
        )