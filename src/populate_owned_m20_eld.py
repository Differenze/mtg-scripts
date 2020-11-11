import json
import ijson

data = dict()
# m20common = []
# m20uncommon = []
# eldcommon = []
# elduncommon = []
# tbdcommon = []

all_cards = "input/meta/all-cards-20201110222017.json"
unique_art_cards = "input/meta/unique-artwork-20201110222247.json"
with open(all_cards, "r", encoding="utf-8") as json_file:
    # data = json.load(json_file)
    objects = ijson.items(json_file, 'item', use_float=True)
    for item in objects:
        if item['lang'] != 'en':
            continue
        if "Basic Land" in item['type_line']:
            continue
        if 'Token' in item['type_line']:
            continue

        if item['set'] in ['m20', 'eld', 'thb'] and\
                item['rarity'] in ['common', 'uncommon']:
            key = item['set']+"_"+item['rarity']
            if key not in data:
                data[key] = []
            data[key].append(item)
        # if 'm20' in item['set'] and 'common' == item['rarity']:
        #     m20common.append(item)
        # if 'm20' in item['set'] and 'uncommon' == item['rarity']:
        #     m20uncommon.append(item)
        # if 'eld' in item['set'] and 'common' == item['rarity']:
        #     eldcommon.append(item)
        # if 'eld' in item['set'] and 'uncommon' == item['rarity']:
        #     elduncommon.append(item)


def write_json(path, filename, data):
    with open(path + filename + ".json", "w") as file:
        # file.write("[\n")
        # file.write("\n".join(map(str, data)))
        # file.write("\n]")
        json.dump(data, file)


def make_txt(card):
    count = 4 if card['rarity'] == 'common' else 1
    return str(count) + " " + card['name']

def write_txt(path, filename, data):
    with open(path + filename+".txt", "w") as file:
        file.write("\n".join(map(make_txt, data)))


folder = "input/owned_cards/"
for key, value in data.items():
    print("creating ", key)
    write_txt(folder+"txt/", key, value)
    write_json(folder+"json/", key, value)

# write_json(folder+"json/", "m20_common", m20common)
# write_json(folder+"json/", "m20_uncommon", m20uncommon)
# write_json(folder+"json/", "eld_common", eldcommon)
# write_json(folder+"json/", "eld_uncommon", elduncommon)
# write_txt(folder+"txt/", "m20_common", m20common)
# write_txt(folder+"txt/", "m20_uncommon", m20uncommon)
# write_txt(folder+"txt/", "eld_common", eldcommon)
# write_txt(folder+"txt/", "eld_uncommon", elduncommon)
