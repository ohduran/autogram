import subprocess

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Pulls media from instagram into the scraped_media folder'

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
            bash_command = command_template.format(bot.username, bot.password, owner)
            process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            if not error:
                # call_command('loadscrapedmedia', 'scraped_media/{}.json'.format(owner))
                self.stdout.write(self.style.SUCCESS('SUCCESS'))
