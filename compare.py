import requests
r = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text': 'It is healthy to start by taking a simple resolve that we will love and care for ourselves. There are few fixed ways of maintaining good health, but it is a subject that demands maximum exploration. Individuals have varied needs, and thus, different measures might work for different people. Starting each day with some free-hand exercise like jogging or running ensures proper blood circulation in the body.Yoga can be a very healthy way of taking your mind off hectic schedules and focus on your spiritual transcendence. One must consume meals at regular intervals and not skip meals, which leads to indigestion and weight gain. Most importantly, keeping a part of your day as “me time” will help to reduce stress. Being healthy facilitates our productivity and ensures that we lead fulfilling lives.',
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())


import requests

url = "https://enelyou-enelyou-summarization--index--summary--topic--part-of-s.p.rapidapi.com/sumpagejson/"

payload = "url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FNatural_language_processing&length=.1"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "0c44d06ccfmshf58c40f536328e0p1deafbjsn272eb2627ff9",
    'x-rapidapi-host': "enelyou-enelyou-summarization--index--summary--topic--part-of-s.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
