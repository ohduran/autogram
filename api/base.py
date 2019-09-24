from logging import getLogger

from django.db.models import F
from InstagramAPI import InstagramAPI
from retrying import retry

log = getLogger(__name__)


class InstagramBot(InstagramAPI):

    url_user_detail = "https://www.instagram.com/%s/"

    def __init__(self, bot, *args, **kwargs):
        super().__init__(username=bot.username,
                         password=bot.pasa,
                         *args, **kwargs)

    @retry(wait_exponential_multiplier=3600000)
    def login(self, force=False):
        return super().login(force)

    def __enter__(self):
        logged_in = self.login()

        if not logged_in:
            if 'error_type' in self.LastJson and self.LastJson['error_type'] == 'sentry_block':
                log.warning('You have been Sentry Blocked!')
            log.warning('You could not be logged in!')
        log.info('Logged in')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.info('Exiting Instagram session')

    def uploadPhoto(self, picture, caption=None, upload_id=None, is_sidecar=None):
        caption_full_text = """{caption}\n\n\n
Great 📸 by {owner}! Thanks for sharing\n\n\n\n\n\n\n\n\n\n\n\n
#barcelona #sightsofbcn #bcn\n\n\n
""".format(caption=caption.text, owner=str(picture.owner))
        super().uploadPhoto(picture.path, caption_full_text, upload_id, is_sidecar)
        picture.times_used = F('times_used') + 1
        picture.save()

        caption.times_used = F('times_used') + 1
        caption.save()
