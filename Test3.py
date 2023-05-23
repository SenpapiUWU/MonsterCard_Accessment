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
    choice = easygui.buttonbox("Options", "Config Menu", ("Add", "Remove", "Search", "Storage", "Exit"))

    if choice == "Add":
        card_name = easygui.enterbox("Enter the card name:")
        if card_name:
            strength = easygui.enterbox("\t\tEnter the strength value: "
                                        "\nValue must be higher or equal to than 0 and lower or equal to 25")
            speed = easygui.enterbox("Enter the speed value:"
                                     "\nValue must be higher or equal to than 0 and lower or equal to 25")
            stealth = easygui.enterbox("Enter the stealth value:"
                                       "\nValue must be higher or equal to than 0 and lower or equal to 25")
            cunning = easygui.enterbox("Enter the cunning value:"
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

    elif choice == "Remove":
        # create an interface for the user to enter the name of the card they want to remove
        card_name = easygui.enterbox("Enter the name of the card you want to remove:")

        if card_name is None:
            continue
        elif card_name not in [creature[0] for creature in creatures]:
            easygui.msgbox("The card doesn't exist.")
        else:
            confirmation = easygui.buttonbox(f"Are you sure you want to remove {card_name}?", "Confirmation", ("Yes", "No"))

            if confirmation == "Yes":
                # find the card in the list and remove it
                for creature in creatures:
                    if creature[0] == card_name:
                        creatures.remove(creature)
                        break
                easygui.msgbox(f"Successfully removed {card_name} from the card list.")
            else:
                easygui.msgbox("Card removal canceled.")

    elif choice == "Storage":
        pass

    elif choice == "Search":
        # display a choice box with options to search by strength, speed, stealth, or cunning
        stat_choice = easygui.buttonbox("Choose a stat to sort by:", "Search Options",
                                        ["Strength", "Speed", "Stealth", "Cunning", "Cancel"])

        if stat_choice == "Cancel":
            continue

        # get the index of the selected stat
        stat_index = ["Strength", "Speed", "Stealth", "Cunning"].index(stat_choice) + 1

        # sort the card list by the selected stat
        sorted_creatures = sorted(creatures, key=lambda card: card[stat_index], reverse=True)

        # create a message string with the sorted card list
        message = "Card name:\tStrength\tSpeed\tStealth\tCunning\n\n\n"
        for creature in sorted_creatures:
            message += f"{creature[0]}\t"
            for stat in creature[1:]:
                message += f"\t{stat}"
            message += "\n\n"

        # output the message using a message box in easygui
        easygui.msgbox(msg=message, title=f"Cards Sorted by {stat_choice}")

    else:
        break
