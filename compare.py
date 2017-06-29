"""
Name       : L Trevor Davies
Program    : Twitter Follower Compare
Date       : June 29th, 2017
"""


from twython import Twython
from twython import TwythonError


def compare(twitter, username):
    followers = twitter.get_followers_ids(screen_name=username)['ids']
    following = twitter.get_friends_ids(screen_name=username)['ids']
    mutual = []
    not_mutual = []
    you_not_back = []

    for i in range(0, len(followers)):
        if followers[i] in following:
            mutual.append(followers[i])
        else:
            not_mutual.append(followers[i])

    for i in range(0, len(not_mutual)):
        if not_mutual[i] in followers:
            you_not_back.append(not_mutual[i])

    print("Users who follow you back")
    print("-------------------------")
    for i in range(0, len(mutual)):
        try:
            print(twitter.lookup_user(user_id=mutual[i])[0]['screen_name'])
        except TwythonError:
            pass

    print()

    print("Users who YOU DON\'T follow back")
    print("--------------------------------")
    for i in range(0, len(you_not_back)):
        try:
            print(twitter.lookup_user(user_id=you_not_back[i])[0]['screen_name'])
        except TwythonError:
            pass


def main():
    consumer_key        = ""	                # Twitter app credentials
    consumer_key_secret = ""
    access_token        = ""
    access_token_secret = ""
    username            = "trevordavies095"
 
    twitter = Twython(consumer_key, consumer_key_secret, access_token, access_token_secret)
    compare(twitter, username)

if __name__ == "__main__":
    main()
