import easygui

# list of the card name
creatures = [
    ["Stoneling", 7, 1, 25, 15],
    ["Vexscream", 1, 6, 21, 19],
    ["Dawnmiraj", 5, 15, 18, 22],
    ["Blazegolm", 15, 20, 23, 6],
    ["Websnake", 7, 15, 10, 5],
    ["Moldvine", 21, 18, 14, 5],
    ["Vortexwing", 19, 13, 19, 2],
    ["Rotthing", 16, 7, 4, 12],
    ["Froststep", 14, 14, 17, 4],
    ["Wispghoul", 17, 19, 3, 2]
]
# create message as an empty string
message = "Creature\t\tStrength\tSpeed\tStealth\tCunning\n\n\n"

# loop through the creatures dictionary and append each creature's stats to the message string
for creature in creatures:
    message += f"{creature[0]}: {creature[1]}\t{creature[2]}\t{creature[3]}\t{creature[4]}\n\n"

# output the message using a message box in easygui
easygui.msgbox(msg=message, title="Catalogue")
