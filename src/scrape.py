import json
import urllib.request

with open("../input/tokens.json") as input_file:
    input_json = json.load(input_file)

    items = input_json["entries"]["columna"]
    for item in items:
        if item["found"]:
            card = item["card_digest"]
            for i in range(0, item["count"]):
                # print(card["image"])
                url = card["image"]
                filename = "../output/"+card["name"]+str(i)+".jpg"
                urllib.request.urlretrieve(url, filename)
