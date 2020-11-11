import sqlite3
from sqlite3 import Error
from pathlib import Path
import json

db_path = "test.db"
# table schema:
# create table card_cache(card_id PRIMARY KEY, card_name, scryfall_json, image_path);

def store_card(card_id, name, card_json, path):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        sql = "insert into card_cache (card_id, card_name, scryfall_json, image_path) values (?,?,?,?)"
        c.execute(sql, (card_id, name, card_json, path))
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()


def get_card_by_id(card_id):
    conn = None
    result = None
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        sql = "select card_id, card_name, scryfall_json, image_path from card_cache where card_id = ?"
        c.execute(sql, (card_id,))
        result = c.fetall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()
    return result


def get_cards_by_name(name):
    conn = None
    result = None
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        sql = "select card_id, card_name, scryfall_json, image_path from card_cache where instr(card_name, ?) > 0"
        c.execute(sql, (name,))
        result = c.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()
    return result


def get_cards_by_json(name):
    conn = None
    result = None
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        sql = "select card_id, card_name, scryfall_json, image_path from card_cache where instr(scryfall_json, ?) > 0"
        c.execute(sql, (name,))
        result = c.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()
    return result


def contains_emerald_image_id(string):
    return "1562929832" in string


def is_green(list):
    return "G" in list


def get_value(dictionary, json_path):
    data = dictionary
    for key in json_path.split("."):
        if key not in data:
            return None
        data = data[key]
    return data


if __name__ == '__main__':
    # with open('mox_jet.json') as mox:
    #     json_data = json.load(mox)
    #     card_id = json_data["id"]
    #     card_name = json_data["name"]
    #     print(card_id)
    #     path = "test"
    #     store_card(card_id, card_name, json.dumps(json_data), path)
    #     output = get_card_by_name("Mox")
    #     for row in output:
    #         print(row[1], json.loads(row[2]))

    for result in get_cards_by_json('"name": "Mox Jet"'):
        print(json.loads(result[2]))
    # path = "color_identity"
    # emerald_dict = json.loads(get_cards_by_name("Emerald")[0][2])
    # jet_dict = json.loads(get_cards_by_name("Jet")[0][2])
    #
    # print("emerald: ", get_value(emerald_dict, path))
    # print("jet: ", get_value(jet_dict, path))
