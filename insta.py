import logging
import os
from random import shuffle
from time import sleep

from instapy import InstaPy
from instapy.util import smart_run
from selenium.common.exceptions import JavascriptException

logger = logging.getLogger('instapy')

if os.environ.get('USERNAME') and os.environ.get('PASSWORD'):
    insta_username = os.environ['USERNAME']
    insta_password = os.environ['PASSWORD']

# dont_like = ['food', 'girl', 'hot']
ignore_words = ['llibertat']
comment_list = ['I love this one!',
                'Great shot!',
                'Nice shot!',
                'I like it so much',
                'Love Barcelona!',
                'Love the view so much!',
                ]
follow_and_like_tag_list = ['#bcn', '#barcelona', '#barcelonaspain', '#barcelonaspain🇪🇸']

bot = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
with smart_run(bot):
    bot.set_relationship_bounds(enabled=True,
                                potency_ratio=-1.21,
                                delimit_by_numbers=True,
                                max_followers=4590,
                                max_following=5555,
                                min_followers=45,
                                min_following=77)
    bot.set_do_comment(True, percentage=90)
    bot.set_comments(comment_list)
    bot.set_do_follow(enabled=True, percentage=10, times=1)
    bot.set_quota_supervisor(enabled=True,
                             peak_likes_hourly=10,
                             peak_follows_hourly=10,
                             peak_unfollows_hourly=10,
                             peak_likes_daily=450,
                             peak_follows_daily=450,
                             peak_unfollows_daily=450,
                             sleep_after=["follows_d", "unfollows_d", "likes_d", "follows_h", "unfollows_h", "likes_h"],
                             stochastic_flow=True,
                             notify_me=True)
    bot.set_action_delays(enabled=True,
                          like=60,
                          comment=59,
                          follow=58,
                          unfollow=57,
                          story=56,
                          random_range_from=70,  # %
                          random_range_to=1000)  # %
    bot.set_dont_unfollow_active_users(enabled=True, posts=5)
    bot.set_ignore_if_contains(ignore_words)

    while True:
        try:
            shuffle(follow_and_like_tag_list)
            bot.like_by_tags(follow_and_like_tag_list, amount=50)
        except (JavascriptException, TypeError):
            logger.warning('Like by tags failed')
        try:
            shuffle(follow_and_like_tag_list)
            bot.unfollow_users(amount=41,
                               instapy_followed_enabled=True,
                               instapy_followed_param="all",
                               style="FIFO",
                               unfollow_after=3*24*60*60,
                               sleep_delay=500)
        except (JavascriptException, TypeError):
            logger.warning('Unfollowing failed')

        logger.info('Sleeping for 8 hours')
        sleep(60*60*8)
        logger.info('Times up')
