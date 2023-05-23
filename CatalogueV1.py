import easygui

# list of the card name
creatures = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmiraj": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolm": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

# make the rows for each category
message = "Creature\tStrength\tSpeed\tStealth\tCunning\n\n"

# loop through the creatures dictionary and append each creature's stats to the message string
for creature, stats in creatures.items():
    message += f"\n{creature}"
    for stat, value in stats.items():
        message += f"\t{value}"

# output the message using a message box in easygui
easygui.msgbox(msg=message, title="Creature Stats")
