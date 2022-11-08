import tweepy

from dotenv import dotenv_values
config = dotenv_values(".env")


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

    api.update_status("Test tweet")


if __name__ == '__main__':
    main()

