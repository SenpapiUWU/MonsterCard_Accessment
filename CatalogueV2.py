import easygui
from Dic import creatures
# make the rows for each category
message = "Creature\t\tStrength\tSpeed\tStealth\tCunning\n\n\n"

# loop through the creatures dictionary and append each creature's stats to the message string
for creature in creatures:
    message += f"{creature[0]}\t"
    for stat in creature[1:]:
        message += f"\t{stat}"
    message += "\n\n"
# output the message using a message box in easygui
easygui.msgbox(msg=message, title="Creature Stats")


