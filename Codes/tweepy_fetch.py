import tweepy
import json


class TweepyFetcher:

    def __init__(self):
        pass

    def fetch(self, id):

        # APP TOKENS
        consumer_key = "MTlxPXxh3WXibQKuwyy6TQvUc"
        consumer_secret = "KMnVvEgQAk9gxlyKC2PtpcllevhqI72rZIouGDL38racclxvj7"
        access_token = "941240160317882369-YlPLfzFUvgoazQHLynmxDx7x8u09mPh"
        access_token_secret = "xWIrTBnIUsdU9cvDlXdIBWg4CEzfIbysBVH4jXO1zosIo"

        # TWEEPY OAUTH
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # PAGE PARAMETERS
        followers = 0
        friends = 0
        avg_retweets = 0
        avg_likes = 0
        bio = 0
        profile_pic = 0
        first_search_result = 0
        retweet_fraction = 0
        avg_no_urls = 0
        isVerified = False

        # API TWEET DATA
        status_list = api.user_timeline(id=id, count=100)
        ct = 0
        tweet_no = 0
        while (ct < 10 and tweet_no < len(status_list)):
            json_dict = json.loads(json.dumps(status_list[tweet_no]._json))
            tweet_no = tweet_no + 1
            if json_dict.get('retweeted_status'):
                continue
            avg_retweets += json_dict['retweet_count']
            avg_likes += json_dict['favorite_count']
            avg_no_urls += json_dict['text'].count("http")
            if json_dict['retweet_count'] > 0:
                retweet_fraction = retweet_fraction + 1
            ct = ct + 1

        if ct != 0:
            avg_retweets /= ct
            avg_likes /= ct
            retweet_fraction /= ct
            avg_no_urls /= ct

        # API BASIC DATA
        json_dict = json.loads(json.dumps(api.get_user(id)._json))
        followers = json_dict['followers_count']
        friends = json_dict['friends_count']
        isVerified = json_dict['verified']
        twitter_id = json_dict['id']
        if json_dict['description'] != "":
            bio = 1
        if json_dict['profile_image_url'] != "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png":
            profile_pic = 1

        # API SEARCH RESULT
        json_dict = json.loads(json.dumps(api.search_users(json_dict['name'])[0]._json))
        if twitter_id == json_dict['id']:
            first_search_result = 1

        return followers, friends, avg_retweets, avg_likes, bio, profile_pic, first_search_result, retweet_fraction,\
               avg_no_urls, isVerified
