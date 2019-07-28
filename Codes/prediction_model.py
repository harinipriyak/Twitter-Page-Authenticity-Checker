from tweepy_fetch import TweepyFetcher
from numpy import array


class Predictor:

    def __init__(self):
        pass

    def predict(self, id, loaded_model):
        # FETCH TWITTER DATA
        (followers, friends, avg_retweets, avg_likes, bio, profile_pic, first_search_result, retweet_fraction,
         avg_no_urls, isVerified) = TweepyFetcher().fetch(id)

        # CHECK IF USER IS VERIFIED
        if isVerified:
            result = 1

        # ELSE CREATE PREDICTION INPUT ARRAY
        else:
            X = self.normalize(avg_likes, avg_no_urls, avg_retweets, bio, first_search_result, followers,
                               friends, profile_pic, retweet_fraction)
            # PERFORM PREDICTION
            prediction = loaded_model.predict(X)
            print(prediction[0][0])
            result = prediction[0][0]
        return result, followers, friends, round(avg_retweets), round(avg_likes)

    @staticmethod
    def normalize(avg_likes, avg_no_urls, avg_retweets, bio, first_search_result, followers, friends,
                  profile_pic, retweet_fraction):
        # NORMALIZATION VARIABLES
        max_followers = 106894244
        max_friends = 619332
        max_avg_retweets = 340312.1
        max_avg_likes = 936155.8
        max_avg_no_urls = 2.3

        # NORMALIZATION OF ATTRIBUTES
        normalized_followers = min((followers / max_followers), 1)
        normalized_friends = min((friends / max_friends), 1)
        if followers + friends != 0:
            followers_ratio = followers / (followers + friends)
            friends_ratio = friends / (followers + friends)
        else:
            followers_ratio = 0
            friends_ratio = 0
        normalized_avg_retweets = min((avg_retweets / max_avg_retweets), 1)
        normalized_avg_likes = min((avg_likes / max_avg_likes), 1)
        normalized_avg_no_urls = avg_no_urls / max_avg_no_urls
        # PREDICTION INPUT ARRAY
        X = array(
            [[normalized_followers, normalized_friends, followers_ratio, friends_ratio, normalized_avg_retweets,
              normalized_avg_likes, bio, profile_pic, first_search_result, retweet_fraction,
              normalized_avg_no_urls]])
        print(X)
        return X
