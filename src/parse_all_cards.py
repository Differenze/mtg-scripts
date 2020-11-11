import json
import ijson

data = []
all_cards = "input/meta/all-cards-20201107101859.json"
unique_art_cards = "input/meta/unique-artwork-20201107102111.json"
with open(unique_art_cards, "r", encoding="utf-8") as json_file:
    # data = json.load(json_file)
    objects = ijson.items(json_file, 'item')
    for item in objects:
        if "Llanowar Elves" in item["name"] and "en" in item["lang"]:
            data.append(item)
            print(item["name"])

print(len(data))
for card in data:
    print(card["set"])
# print(len(data))
# for card in data:
#     print(card["name"])
