import requests
import pprint
import json

#data = requests.get("https://tools.wmflabs.org/datacon-schedule-app/sessions.json").json()
#with open('data.json', 'w') as f:
#    json.dump(data, f)

with open('data.json') as f:
    data = json.load(f)

for key in data.keys():
    print(key)
pprint.pprint(data)

for session in data["sessions"]:
    category = session["category"]
    day = session["day"]
    description = session["description"]
    duration = session["duration"]
    facilitator_array = session["facilitator_array"]
    facilitator = session["facilitators"]
    link = session["link"]
    location = session["location"]
    start = session["start"]
    title = session["title"]
    timeblock = session["timeblock"]
    tags = session["tags"]
    print(session.keys())