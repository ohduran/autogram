from json import load
from re import findall

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import IntegrityError

from ....owners.models import Owner
from ...models import Picture

User = get_user_model()


class Command(BaseCommand):
    help = 'Pulls media from scraped_media folder into database'

    def add_arguments(self, parser):
        """python manage.py loadmedia scraped_media/demo_ig_scraper.json"""
        parser.add_argument('files', nargs='+', type=str)

    def handle(self, *args, **options):
        """
        Load data from the files and uploads pictures in pictures.Picture table.
        """
        user = User.objects.first()

        loaded = 0
        for file in options['files']:
            with open(file) as j:
                data = load(j)['GraphImages']

            for picture in data:

                owner_data = {
                    'username': self._picture_owner(picture),
                    'instagram_id': picture['owner']['id'],
                    'user': user
                }
                owner, _ = Owner.objects.update_or_create(**owner_data)

                picture_name = self._picture_name(picture['display_url'])
                try:
                    with open(f'scraped_media/{picture_name}.jpg', 'rb') as file:
                        picture_data = {
                            'likes': picture['edge_media_preview_like']['count'],
                            'comments': picture['edge_media_to_comment']['count'],
                            'owner': owner,
                            'user': user,
                        }
                        try:
                            picture, created = Picture.objects.update_or_create(name=picture_name, defaults=picture_data)

                            if created:
                                picture.file.save(picture_name, ContentFile(file.read()))
                                loaded += 1
                        except IntegrityError:
                            self.stdout.write(self.style.WARNING('Attempt to upload a picture without name'))
                except FileNotFoundError:
                    pass
            self.stdout.write(self.style.SUCCESS(f"{loaded} pictures loaded"))

    def _picture_name(self, display_url):
        name = findall('(?:\/e35\/)(\S+).jpg', display_url)
        if not name:
            return None
        return name[0]

    def _picture_owner(self, picture):
        caption_edges = picture['edge_media_to_caption'].get('edges')
        if caption_edges:
            caption = caption_edges[0]['node']['text']
            return findall('(?:@)(\w+)', caption)[0] if findall('(?:@)(\w+)', caption) else picture['username']
