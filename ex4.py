import json as json
import requests as req

APIlist = []

for i in range(1,6):
    API = req.get("https://catfact.ninja/fact")
    if API.status_code == 200:
        data = API.json()
        APIlist.append(data)
    else:
        print(f"Error: Status code {API.status_code}")

#print(APIlist)

jsonAPI = json.dumps(APIlist)

#print(jsonAPI)

for object in APIlist:
     print(object)

