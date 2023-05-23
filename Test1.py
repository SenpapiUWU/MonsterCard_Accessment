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
    choice = easygui.buttonbox("Options", "Config Menu", ("Add", "Remove", "Search", "Storage", "Exit"))

    if choice == "Add":
        card_name = easygui.enterbox("Enter the card name:")
        if card_name:
            strength = easygui.enterbox("Enter the strength value:")
            speed = easygui.enterbox("Enter the speed value:")
            stealth = easygui.enterbox("Enter the stealth value:")
            cunning = easygui.enterbox("Enter the cunning value:")

            creatures.append([card_name, strength, speed, stealth, cunning])
    elif choice == "Remove":
        card_name = easygui.enterbox("Enter the card name to remove:")
        for creature in creatures:
            if creature[0] == card_name:
                creatures.remove(creature)
                break
    elif choice == "Search":
        card_name = easygui.enterbox("Enter the card name to search:")
        found = False
        for creature in creatures:
            if creature[0] == card_name:
                easygui.msgbox(msg=f"Card name: {creature[0]}\nStrength: {creature[1]}\nSpeed: "
                                   f"{creature[2]}\nStealth: {creature[3]}\nCunning: {creature[4]}",
                               title="Card Details")
                found = True
                break
        if not found:
            easygui.msgbox(msg="Card not found!", title="Error")
    elif choice == "Storage":
        pass
    else:
        break
