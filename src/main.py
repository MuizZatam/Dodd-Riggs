from modules.gemini import generate_tweet
from modules.api import create_tweet


def main():
    tweet = generate_tweet(
        "You are Dodd Riggs. Here's your bio: 'Retired engineer on a Nebraska ranch. I fix tractors, curse at the wind, and tweet like it's a contact sport.' Generate a single, <100 word tweet describing yourself to twitter with the general tone of your bio"
    )
    print(tweet)
    response = create_tweet(tweet)
    print(response)


if __name__ == "__main__":
    main()
