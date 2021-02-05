import tweepy
import config

def main():
    auth = tweepy.OAuthHandler(*config.consumer.values())
    auth.set_access_token(*config.access_token.values())

    api = tweepy.API(auth)


if __name__ == '__main__':
    main()
