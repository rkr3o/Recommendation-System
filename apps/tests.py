from django.test import TestCase
from keys.third_party_api_keys import Constants

keys = Constants.ThirdParty.OpenAi.KEY
from openai import OpenAI

client = OpenAI(keys)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

print(completion.choices[0].message)
