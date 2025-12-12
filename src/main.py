from modules.gemini import generate_tweet
from modules.api import create_tweet
from modules.prompt import get_random_prompt


def main():
    prompt = get_random_prompt()

    tweet = generate_tweet(prompt=prompt)

    print(tweet)

    response = create_tweet(tweet)

    print(response)


if __name__ == "__main__":
    main()
