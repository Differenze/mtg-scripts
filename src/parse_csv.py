import csv
folder = "input/jumpstart/budget_decks/battle_box_silverblood/"
file = "JumpstartBattleBox.csv"


def get_name(card):
    return "1 "+card['Name']


decks = dict()
with open(folder+file) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for line in reader:
        deck = line['Tags']
        if deck not in decks:
            decks[deck] = []
        decks[deck].append(line)


for name in decks:
    with open(folder+"decks/"+name+".txt", "w") as deckfile:
        deck = '\n'.join(map(get_name, decks[name]))
        deckfile.write(deck)

