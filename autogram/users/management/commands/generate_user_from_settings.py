from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generates a base user from the settings'

    def handle(self, *args, **options):
        if getattr(settings, 'USERNAME', None) and getattr(settings, 'PASSWORD', None):
            try:
                User.objects.create_user(username=settings['USERNAME'], password=settings['PASSWORD'])
            except IntegrityError:
                self.stdout.write(self.style.WARNING('User already created from settings'))
        else:
            self.stdout.write(self.style.ERROR('There are no Username or Password on your environment variables'))
