from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def generate_tweet(prompt: str) -> str:
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    return response.text


if __name__ == "__main__":
    print(generate_tweet("Give an unhinged opinion about Java lovers"))
