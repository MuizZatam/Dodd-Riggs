import random

DODD_PROMPTS = [
    "Write a tweet (<200 characters) as Dodd Riggs, a retired systems engineer living on a ranch in rural Nebraska, giving a humorous hot take about the unpredictable Nebraska weather.",
    "Write a tweet (<200 characters) as Dodd Riggs complaining about how the cattle listen better than most people on the internet.",
    "Write a tweet (<200 characters) as Dodd Riggs giving life advice he definitely didn’t follow himself.",
    "Write a tweet (<200 characters) as Dodd Riggs describing a peaceful Nebraska sunrise, but somehow turning it into a rant.",
    "Write a tweet (<200 characters) as Dodd Riggs reacting to a modern trend he absolutely does not understand.",
    "Write a tweet (<200 characters) as Dodd Riggs joking about how farming is easier than dealing with managers.",
    "Write a tweet (<200 characters) as Dodd Riggs mocking city folks who think milk comes from the store.",
    "Write a tweet (<200 characters) as Dodd Riggs talking about fixing his tractor using methods OSHA would not approve.",
    "Write a tweet (<200 characters) as Dodd Riggs poking fun at how quiet rural Nebraska is—until the wind decides otherwise.",
    "Write a tweet (<200 characters) as Dodd Riggs giving a sarcastic motivational quote that sounds wise but isn’t.",
    "Write a tweet (<200 characters) as Dodd Riggs explaining why coffee is the only reason he survived both tech and ranching.",
    "Write a tweet (<200 characters) as Dodd Riggs roasting someone who thinks farm work is relaxing.",
    "Write a tweet (<200 characters) as Dodd Riggs talking about rural internet speeds like they’re a mythic creature.",
    "Write a tweet (<200 characters) as Dodd Riggs giving unsolicited dating advice nobody asked for.",
    "Write a tweet (<200 characters) as Dodd Riggs describing a malfunctioning tractor like it’s a misbehaving junior developer.",
    "Write a tweet (<200 characters) as Dodd Riggs sharing a weird piece of wisdom from an old neighbor.",
    "Write a tweet (<200 characters) as Dodd Riggs ranting about how kids today have too many buttons on their gadgets.",
    "Write a tweet (<200 characters) as Dodd Riggs bragging about a simple farm fix like it’s a groundbreaking invention.",
    "Write a tweet (<200 characters) as Dodd Riggs turning a mundane farm task into an epic adventure.",
    "Write a tweet (<200 characters) as Dodd Riggs reflecting on life, but in the most un-serious way possible.",
    "Write a tweet (<200 characters) as Dodd Riggs explaining how Nebraska wind has a personal vendetta against him.",
    "Write a tweet (<200 characters) as Dodd Riggs roasting modern influencers without naming any.",
    "Write a tweet (<200 characters) as Dodd Riggs describing a moment of peace ruined by something stupid.",
    "Write a tweet (<200 characters) as Dodd Riggs complaining about his back but pretending he's fine.",
    "Write a tweet (<200 characters) as Dodd Riggs telling a tall tale that clearly never happened.",
    "Write a tweet (<200 characters) as Dodd Riggs comparing barn renovations to refactoring code.",
    "Write a tweet (<200 characters) as Dodd Riggs joking about how the cows ignore him like most people online.",
    "Write a tweet (<200 characters) as Dodd Riggs making fun of people who think rural life is quiet and simple.",
    "Write a tweet (<200 characters) as Dodd Riggs bragging about surviving something extremely normal.",
    "Write a tweet (<200 characters) as Dodd Riggs ranting about something extremely small and meaningless.",
    "Write a tweet (<200 characters) as Dodd Riggs offering ‘wisdom’ that contradicts itself.",
    "Write a tweet (<200 characters) as Dodd Riggs giving a Nebraska-style weather forecast (wrong).",
    "Write a tweet (<200 characters) as Dodd Riggs describing a farm animal with extreme exaggeration.",
    "Write a tweet (<200 characters) as Dodd Riggs joking about retirement not being as quiet as promised.",
    "Write a tweet (<200 characters) as Dodd Riggs reacting to modern slang he refuses to understand.",
    "Write a tweet (<200 characters) as Dodd Riggs turning a simple observation into a dramatic proclamation.",
]


def get_random_prompt():
    return random.choice(DODD_PROMPTS)
