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

    elif choice == "Remove":
        # create an interface for the user to enter the name of the card they want to remove
        card_name = easygui.enterbox("Enter the name of the card you want to remove:")

        if card_name is None:
            continue
        elif card_name not in [creature[0] for creature in creatures]:
            easygui.msgbox("The card doesn't exist.")
        else:
            confirmation = easygui.buttonbox(f"Are you sure you want to remove {card_name}?",
                                             "Confirmation", ("Yes", "No"))

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
    elif choice == "Edit":
        # create a list of creature names for the choice box
        creature_names = [creature[0] for creature in creatures]

        # display a choice box with the creature names
        selected_creature = easygui.choicebox("Select a creature to edit:", "Edit Creature", creature_names)

        if selected_creature is None:
            easygui.msgbox("No creature selected")
        else:
            # find the selected creature in the list
            found_creature = None
            for creature in creatures:
                if creature[0] == selected_creature:
                    found_creature = creature
                    break

            if found_creature is None:
                easygui.msgbox(f"Creature '{selected_creature}' not found in the creature list!")
            else:
                # create an interface for the user to enter the new stats for the creature
                card_name = selected_creature
                strength = easygui.enterbox(f"\tEnter the new strength value for '{card_name}':"
                                            "\nValue must be higher or equal to than 0 and lower or equal to 25",
                                            default=str(found_creature[1]))
                speed = easygui.enterbox(f"\tEnter the new speed value for '{card_name}':"
                                         "\nValue must be higher or equal to than 0 and lower or equal to 25",
                                         default=str(found_creature[2]))
                stealth = easygui.enterbox(f"\tEnter the new stealth value for '{card_name}':"
                                           "\nValue must be higher or equal to than 0 and lower or equal to 25",
                                           default=str(found_creature[3]))
                cunning = easygui.enterbox(f"\tEnter the new cunning value for '{card_name}':"
                                           "\nValue must be higher or equal to than 0 and lower or equal to 25",
                                           default=str(found_creature[4]))

                if strength is None or speed is None or stealth is None or cunning is None:
                    easygui.msgbox("Invalid input: Please enter valid stats.")
                else:
                    try:
                        strength = int(strength)
                        speed = int(speed)
                        stealth = int(stealth)
                        cunning = int(cunning)

                        if 0 <= strength <= 25 and 0 <= speed <= 25 and 0 <= stealth <= 25 and 0 <= cunning <= 25:
                            found_creature[1:] = [strength, speed, stealth, cunning]
                            easygui.msgbox(f"Updated stats for {card_name}!")
                        else:
                            easygui.msgbox("Invalid Stats: Stats must be integers between 0 and 25")
                    except ValueError:
                        easygui.msgbox("Invalid Stats: Stats must be integers")
    elif choice == "Search":

        # display a choice box with options to search by strength, speed, stealth, or cunning

        stat_choice = easygui.buttonbox("Please select search options", "Search Options",
                                        ["Sort by stats", "Search by name", "Cancel"])
        if stat_choice == "Cancel":
            continue

        if stat_choice == "Search by name":

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
                easygui.msgbox("Card not found.")
        elif stat_choice == "Sort by stats":
            stat_sort_choice = easygui.buttonbox("Please select the stats to be sorted", "Sorted stats",
                                                 choices=["Strength", "Speed", "Stealth", "Cunning"])

            # get the index of the selected stat
            stat_index = ["Strength", "Speed", "Stealth", "Cunning"].index(stat_sort_choice) + 1

            # sort the card list by the selected stat
            sorted_creatures = sorted(creatures, key=lambda card: card[stat_index], reverse=True)

            # create a message string with the sorted card list
            message = "Card name:\tStrength\tSpeed\tStealth\tCunning\n\n\n"

            for creature in sorted_creatures:
                message += f"{creature[0]}\t"

                for stat in creature[1:]:
                    message += f"\t{stat}"

                message += "\n\n"

            easygui.msgbox(msg=message, title="Sorted Card List")
    else:
        break
