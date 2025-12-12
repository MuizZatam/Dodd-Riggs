from modules.gemini import generate_tweet
from modules.api import create_tweet, reply_to_tweet, get_mentions, load_replied_tweets, save_replied_tweet
from modules.prompt import get_random_prompt


def reply_to_mentions():

    replied_tweets = load_replied_tweets()
    print(f"Already replied to {len(replied_tweets)} tweets\n")

    
    mentions = get_mentions(max_results=10)

    if not mentions:
        print("No mentions to reply to.")
        return

    new_mentions = [m for m in mentions if str(m['id']) not in replied_tweets]

    print(f"Found {len(new_mentions)} mentions\n")

    for mention in new_mentions:
        print(f"@{mention['author_username']}: {mention['text']}")

        prompt = f"""You are Dodd Riggs — a retired engineer living on a windy Nebraska ranch. You fix tractors, gripe about the weather, and treat Twitter like a full-contact sport. Someone tweeted at you: "{mention["text"]}Write a brief reply (under 200 characters) in Dodd’s voice. Be grumpy, clever, and authentic. No hashtags, no emojis, and no politeness unless it’s sarcastic."""

        reply = generate_tweet(prompt)

        if not reply.startswith(f"@{mention['author_username']}"):
            reply = f"@{mention['author_username']} {reply}"

        response = reply_to_tweet(mention["id"], reply)

        save_replied_tweet(mention['id'])

    print(response)


def post_usual_tweet():
    prompt = get_random_prompt()

    tweet = generate_tweet(prompt=prompt)

    print(tweet)

    response = create_tweet(tweet)

    print(response)


def main():
    reply_to_mentions()
    post_usual_tweet()


if __name__ == "__main__":
    main()
