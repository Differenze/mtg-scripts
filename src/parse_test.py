import json
import ijson

data = []
m20common = []
m20uncommon = []
eldcommon = []
elduncommon = []
all_cards = "input/meta/all-cards-20201110222017.json"
unique_art_cards = "input/meta/unique-artwork-20201110222247.json"
input_cards = "input/owned_cards/m20_common.json"
with open(input_cards, "r", encoding="utf-8") as json_file:
    # data = json.load(json_file)
    objects = ijson.items(json_file, 'item')
    for item in objects:
        if item['lang'] != 'en':
            continue
        if "Basic Land" in item['type_line']:
            continue
        if 'Token' in item['type_line']:
            continue
        if 'm20' in item['set'] and 'common' == item['rarity']:
            m20common.append(item)
        if 'm20' in item['set'] and 'uncommon' == item['rarity']:
            m20uncommon.append(item)
        if 'eld' in item['set'] and 'common' == item['rarity']:
            eldcommon.append(item)
        if 'eld' in item['set'] and 'uncommon' == item['rarity']:
            elduncommon.append(item)


def test(card):
    return card['name']


print('\n'.join(map(test, m20common)))
