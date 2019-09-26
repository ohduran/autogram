import subprocess

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Pulls media from instagram into the scraped_media folder'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        """python manage.py scrapmedia demo_ig_scraper"""
        parser.add_argument('owners', nargs='+', type=str)

    def handle(self, *args, **options):
        """
        instagram-scraper -u settings.BOT_USERNAME -p settings.BOT_PASSWORD sightsofbcn -d scraped_media --media-metadata

        And then, call_command loadscrapedmedia on the resulting file.
        """
        command_template = 'instagram-scraper -u {} -p {} {} -d scraped_media --media-metadata'

        for owner in options['owners']:
            bot = User.objects.first()
            bash_command = command_template.format(bot.username, bot.para, owner)
            self.stdout.write(self.style.WARNING(f'Now running {bash_command}'))
            process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            if not error:
                self.stdout.write(self.style.WARNING('Loading scraped media from scraped_media/{}.json'.format(owner)))
                call_command('loadmedia', 'scraped_media/{}.json'.format(owner))
