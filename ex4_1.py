import json as json
import requests as req

APIresponse = req.get("https://api.github.com/search/repositories?q=language:python")

data = APIresponse.json()

items = data["items"]

items.sort(key=lambda x: x['forks'], reverse = True)

for dict in items:
    name = dict["name"]
    description = dict["description"]
    forks = dict["forks"]
    print(f"Forks:{forks}. Name:{name} Description:{description}")
