import easygui
from Dic import creatures

while True:
    # make the rows for each category
    message = "Card name:\tStrength\tSpeed\tStealth\tCunning\n\n\n"

    # get info from the creatures dictionary and append each creature's stats to the message string
    for creature in creatures:
        message += f"{creature[0]}\t"
        for stat in creature[1:]:
            message += f"\t{stat}"
        message += "\n\n"

    # output the message using a message box in easygui
    easygui.msgbox(msg=message, title="Card Stats")

    # display a button box with options to add, remove, or exit
    choice = easygui.buttonbox("Options", "Config Menu", ("Add", "Remove", "Search", "Storage", "Edit", "Exit"))

    if choice == "Remove":
        card_name = easygui.enterbox("Enter the card name to remove:")
    for creature in creatures:
        if creature[0] == card_name:
            creatures.remove(creature)

    if choice == "Exit":
        break
