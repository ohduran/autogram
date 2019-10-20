import logging
import os
from random import shuffle

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
follow_and_like_tag_list = ['bcn', '#barcelona', '#barcelonaspain', '#barcelonaspain🇪🇸']

bot = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
with smart_run(bot):
    bot.set_relationship_bounds(enabled=True,
                                potency_ratio=-1.21,
                                delimit_by_numbers=True,
                                max_followers=4590,
                                max_following=5555,
                                min_followers=45,
                                min_following=77)
    bot.set_do_comment(True, percentage=10)
    bot.set_comments(comment_list)
    bot.set_quota_supervisor(enabled=True,
                             peak_likes_hourly=20,
                             peak_likes_daily=450,
                             peak_follows_daily=560,
                             peak_follows_hourly=56,
                             peak_unfollows_hourly=49,
                             peak_unfollows_daily=550,
                             sleep_after=["follows_h", "unfollows_d", "likes_h", "likes_d"],
                             stochastic_flow=True,
                             notify_me=True)
    bot.set_action_delays(enabled=True,
                          like=60,
                          comment=5,
                          follow=4.5,
                          unfollow=28,
                          story=10,
                          random_range_from=70,  # %
                          random_range_to=130)  # %
    bot.set_dont_unfollow_active_users(enabled=True, posts=5)
    bot.set_ignore_if_contains(ignore_words)

    while True:
        try:
            bot.like_by_tags(follow_and_like_tag_list, amount=50)
        except (JavascriptException, TypeError):
            logger.debug('Like by tags failed')
        # follow_and_like_tag_list = shuffle(follow_and_like_tag_list)
        try:
            bot.follow_by_tags(follow_and_like_tag_list, amount=50, interact=True)
        except (JavascriptException, TypeError):
            logger.debug('Follow by tags failed')
        try:
            bot.unfollow_users(amount=50,
                               instapy_followed_enabled=True,
                               instapy_followed_param="all",
                               style="FIFO",
                               unfollow_after=3*24*60*60,
                               sleep_delay=500)
        except (JavascriptException, TypeError):
            logger.debug('Unfollowing failed')

        # try:
        #     bot.set_do_story(enabled=True, percentage=70, simulate=False)
        # except (JavascriptException, TypeError):
        #     pass
        # try:
        #     bot.story_by_tags(follow_and_like_tag_list, amount=100)
        # except (JavascriptException, TypeError):
        #     pass

        # try:
        #     bot.follow_by_tags(follow_and_like_tag_list, amount=400, interact=True)
        # except (JavascriptException, TypeError):
        #     pass
        # try:
        #     bot.unfollow_users(amount=400, allFollowing=True, style='RANDOM', unfollow_after=2*24*60)
        # except (JavascriptException, TypeError):
        #     pass
