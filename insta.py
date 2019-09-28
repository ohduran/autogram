import os

from instapy import InstaPy
from instapy.util import smart_run

# Write your automation here
# Stuck ? Look at the github page or the examples in the examples folder
if os.environ.get('USERNAME') and os.environ.get('PASSWORD'):
    insta_username = os.environ['USERNAME']
    insta_password = os.environ['PASSWORD']

# dont_like = ['food', 'girl', 'hot']
ignore_words = ['pizza']
comment_list = ['I love this one!', 'Nice shot!', 'I like it so much']
follow_and_like_tag_list = ['bcn', '#barcelona', '#barcelonaspain', '#barcelonaspain🇪🇸']
# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")

bot = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
with smart_run(bot):
    while True:
        bot.set_relationship_bounds(enabled=True,
                                    potency_ratio=-1.21,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    max_following=5555,
                                    min_followers=45,
                                    min_following=77)
        bot.set_do_comment(True, percentage=1)
        bot.set_comments(comment_list)
        bot.set_quota_supervisor(enabled=True, peak_follows_daily=560, peak_follows_hourly=56, peak_unfollows_hourly=49, peak_unfollows_daily=550, sleep_after=["follows_h", "unfollows_d"], stochastic_flow=True, notify_me=True)
        bot.set_dont_unfollow_active_users(enabled=True, posts=5)
        bot.set_ignore_if_contains(ignore_words)
        bot.like_by_tags(follow_and_like_tag_list, amount=1000)
        bot.follow_by_tags(follow_and_like_tag_list, amount=400, sleep_delay=600, interact=True)
        bot.unfollow_users(amount=400, instapy_followed_enabled=True, instapy_followed_param='all', style='RANDOM', unfollow_after=2*24*60)
