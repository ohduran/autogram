from logging import getLogger

from django.db.models import F
from InstagramAPI import InstagramAPI
from retrying import retry

log = getLogger(__name__)


class InstagramBot(InstagramAPI):

    url_user_detail = "https://www.instagram.com/%s/"

    def __init__(self, bot, *args, **kwargs):
        super().__init__(username=bot.username,
                         password=bot.para,
                         *args, **kwargs)

    @retry(wait_exponential_multiplier=3600000)
    def login(self, force=False):
        return super().login(force)

    def __enter__(self):
        logged_in = self.login()

        if not logged_in:
            if 'error_type' in self.LastJson and self.LastJson['error_type'] == 'sentry_block':
                log.warning('You have been Sentry Blocked!')
            elif 'message' in self.LastJson and self.LastJson['message'] == 'challenge_required':
                log.warning('Challenge required')
                raise Exception
            log.warning('You could not be logged in!')
        log.info('Logged in')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.info('Exiting Instagram session')
        self.logout()

    def uploadPicture(self, picture, caption):
        caption_full_text = """{caption}\n\n\n
Great 📸 by {owner}! Thanks for sharing\n\n\n\n\n\n\n\n\n\n\n\n
#barcelona #sightsofbcn #bcn\n\n\n
""".format(caption=caption.text, owner=str(picture.owner))
        if self.uploadPhoto(picture.path, caption_full_text, upload_id=None, is_sidecar=None):
            log.info(f'Picture by {picture.owner} uploaded')
            log.info(f'Caption used: {caption.text}')
            picture.times_used = F('times_used') + 1
            picture.save()

            caption.times_used = F('times_used') + 1
            caption.save()
            log.info('Picture uploaded!')
        else:
            log.info(f'There was an error and the picture could not be loaded')
