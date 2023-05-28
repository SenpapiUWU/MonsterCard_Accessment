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

    # display a button box with options to add, remove, search, or exit
    choice = easygui.buttonbox("Options", "Config Menu", ("Add", "Remove", "Search", "Storage", "Edit", "Exit"))

    if choice == "Add":
        card_name = easygui.enterbox("Enter the card name:")
        if card_name:
            strength = easygui.enterbox("\t\tEnter the strength value: "
                                        "\nValue must be higher or equal to than 0 and lower or equal to 25")
            speed = easygui.enterbox("\t\tEnter the speed value:"
                                     "\nValue must be higher or equal to than 0 and lower or equal to 25")
            stealth = easygui.enterbox("\t\tEnter the stealth value:"
                                       "\nValue must be higher or equal to than 0 and lower or equal to 25")
            cunning = easygui.enterbox("\t\tEnter the cunning value:"
                                       "\nValue must be higher or equal to than 0 and lower or equal to 25")

            if strength and speed and stealth and cunning:
                try:
                    strength = int(strength)
                    speed = int(speed)
                    stealth = int(stealth)
                    cunning = int(cunning)

                    if 0 <= strength <= 25 and 0 <= speed <= 25 and 0 <= stealth <= 25 and 0 <= cunning <= 25:
                        creatures.append([card_name, strength, speed, stealth, cunning])
                        easygui.msgbox(f"Added {card_name} to the card list")
                    else:
                        easygui.msgbox("Invalid Stats: Stats must be integers between 0 and 25")
                except ValueError:
                    easygui.msgbox("Invalid Stats: Stats must be integers")
            else:
                easygui.msgbox("Invalid input: Please enter valid stats.")
        elif choice == "cancel":
            continue
    else:
        break



#

