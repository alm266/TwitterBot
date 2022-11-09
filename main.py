import tweepy

from dotenv import dotenv_values

from library.dictionaryOutputHandler import generate_tweet_text

config = dotenv_values(".env")

from PyDictionary import PyDictionary
dictionary = PyDictionary()


def main():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(
        config.get("api_key"),
        config.get("api_key_secret")
    )
    auth.set_access_token(
        config.get("access_token"),
        config.get("access_token_secret")
    )

    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
        return

    tweet_string = generate_tweet_text()
    api.update_status(tweet_string)
    print(tweet_string)


if __name__ == '__main__':
    main()

