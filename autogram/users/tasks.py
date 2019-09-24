from api import InstagramBot
from config import celery_app
from django.contrib.auth import get_user_model

User = get_user_model()


@celery_app.task()
def upload_picture():
    """Upload a picture to Instagram."""
    user = User.objects.first()

    picture = user.picture_set.least_used().random().get()
    caption = user.caption_set.least_used().random().get()

    with InstagramBot(bot=user) as instabot:
        instabot.uploadPhoto(picture, caption=caption)
