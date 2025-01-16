#1_1
import json as json

#1_2
item = {
    "name": "Book of the knowledge",
    "rarity": "common",
    "durability": 100,
}

#1_3
json_item = json.dumps(item)

#1_4
item2 = json.loads(json_item)

#1_5
with open("ex3.json", "w") as jsonfile:
    json.dump(item, jsonfile, indent=4)

#1_6
with open("ex3.json", "r") as jsonfile:
    item3 = json.load(jsonfile)

#print(item3["name"])

#2_1
item["price"] = 1000

#2_2
item["sellers"] =["John", "Peter", "Mary"]

#2_3
item["description"] = {
    "text": "This is a book of knowledge",
    "author": "Unknown",
    "importantPages": [33, 44, 555]
}

#2_4
print(item)
print()

#2_5
print(item["price"])
print()
#2_6
print(item["sellers"][1])
print()

#2_7
print(item["description"]["importantPages"][2])
print()

#2_8
desc = item["description"]["text"]
importantpage = item["description"]["importantPages"][2]

print(f"Description: {desc} \nBookmarked page: {importantpage}")
print()

#2_9
deletelist = ["price","sellers","description"]

for key in deletelist:
    del item[key]

print(item)
