from dotenv import load_dotenv
import os
import tweepy

load_dotenv()

client = tweepy.Client(
    consumer_key=os.environ.get("CONSUMER_KEY"),
    consumer_secret=os.environ.get("CONSUMER_SECRET"),
    access_token=os.environ.get("ACCESS_TOKEN"),
    access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET"),
    bearer_token=os.environ.get("BEARER_TOKEN"),
)


def create_tweet(content):
    response = client.create_tweet(text=content)
    return response


def get_mentions(max_results=10):
    me = client.get_me()
    user_id = me.data.id

    mentions = client.get_users_mentions(
        id=user_id,
        max_results=max_results,
        tweet_fields=["created_at", "conversation_id", "author_id"],
        expansions=["author_id"],
    )

    if not mentions.data:
        print("No mentions found")
        return []

    users = {user.id: user.username for user in mentions.includes["users"]}

    tweets = []

    for tweet in mentions.data:
        tweets.append(
            {
                "id": tweet.id,
                "text": tweet.text,
                "author_id": tweet.author_id,
                "author_username": users.get(tweet.author_id, "unknown"),
                "conversation_id": tweet.conversation_id,
                "created_at": tweet.created_at,
            }
        )

    return tweets


def reply_to_tweet(tweet_id, reply_text):
    response = client.create_tweet(text=reply_text, in_reply_to_tweet_id=tweet_id)

    return response

def load_replied_tweets():
    with open('replied_tweets.txt', 'r') as f:
        return set(line.strip() for line in f)

def save_replied_tweet(tweet_id):
    with open('replied_tweets.txt', 'a') as f:
        f.write(f"{tweet_id}\n")
