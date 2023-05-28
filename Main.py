import easygui
from Dic import creatures


def display_card_stats():
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


def add_card():
    card_name = easygui.enterbox("Enter the card name:")

    if not card_name:
        return  # User canceled, do nothing

    strength = easygui.enterbox(f"\tEnter the new strength value for '{card_name}':"
                                "\nValue must be higher or equal to than 0 and lower or equal to 25")
    if strength is None:
        easygui.msgbox("Adding canceled for creature: " + card_name)
        return  # User canceled, do nothing
    if not strength:
        return

    speed = easygui.enterbox(f"\tEnter the new speed value for '{card_name}':"
                             "\nValue must be higher or equal to than 0 and lower or equal to 25")
    if speed is None:
        easygui.msgbox("Adding canceled for creature: " + card_name)
        return  # User canceled, do nothing
    if not speed:
        return

    stealth = easygui.enterbox(f"\tEnter the new stealth value for '{card_name}':"
                               "\nValue must be higher or equal to than 0 and lower or equal to 25")
    if stealth is None:
        easygui.msgbox("Adding canceled for creature: " + card_name)
        return  # User canceled, do nothing
    if not stealth:
        return

    cunning = easygui.enterbox(f"\tEnter the new cunning value for '{card_name}':"
                               "\nValue must be higher or equal to than 0 and lower or equal to 25")
    if cunning is None:
        easygui.msgbox("Adding canceled for creature: " + card_name)
        return  # User canceled, do nothing
    if not cunning:
        return

    try:
        strength = int(strength)
        speed = int(speed)
        stealth = int(stealth)
        cunning = int(cunning)

        if 0 <= strength <= 25 and 0 <= speed <= 25 and 0 <= stealth <= 25 and 0 <= cunning <= 25:
            creatures.append([card_name, strength, speed, stealth, cunning])
            easygui.msgbox(f"Successfully added {card_name} to the list!")
        else:
            easygui.msgbox("Invalid Stats: Stats must be integers between 0 and 25")
    except ValueError:
        easygui.msgbox("Invalid Stats: Stats must be integers")


def remove_card():
    # create an interface for the user to enter the name of the card they want to remove
    card_name = easygui.enterbox("Enter the name of the card you want to remove:")

    if card_name is None:
        return
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


def edit_card():
    # create a list of creature names for the choice box
    creature_names = [creature[0] for creature in creatures]

    # display a choice box with the creature names
    selected_creature = easygui.choicebox("Select a creature to edit:", "Edit Creature", creature_names)

    if selected_creature is None:
        easygui.msgbox("No creature selected")
        return  # Return or perform necessary actions for cancel scenario

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

            if strength is None:
                easygui.msgbox("Editing canceled for creature: " + card_name)
                return  # Return or perform necessary actions for cancel scenario
            if not strength:
                return
            speed = easygui.enterbox(f"\tEnter the new speed value for '{card_name}':"
                                     "\nValue must be higher or equal to than 0 and lower or equal to 25",
                                     default=str(found_creature[2]))
            if not speed:
                return
            if speed is None:
                easygui.msgbox("Editing canceled for creature: " + card_name)
                return  # Return or perform necessary actions for cancel scenario

            stealth = easygui.enterbox(f"\tEnter the new stealth value for '{card_name}':"
                                       "\nValue must be higher or equal to than 0 and lower or equal to 25",
                                       default=str(found_creature[3]))
            if not stealth:
                return
            if stealth is None:
                easygui.msgbox("Editing canceled for creature: " + card_name)
                return  # Return or perform necessary actions for cancel scenario

            cunning = easygui.enterbox(f"\tEnter the new cunning value for '{card_name}':"
                                       "\nValue must be higher or equal to than 0 and lower or equal to 25",
                                       default=str(found_creature[4]))
            if not cunning:
                return
            if cunning is None:
                easygui.msgbox("Editing canceled for creature: " + card_name)
                return  # Return or perform necessary actions for cancel scenario

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


def search_card():
    # display a choice box with options to search by strength, speed, stealth, or cunning
    stat_choice = easygui.buttonbox("Please select search options", "Search Options",
                                    ["Sort by stats", "Search by name", "Cancel"])
    if stat_choice == "Cancel":
        return

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
        stat_index = ["Strength", "Speed", "Stealth", "Cunning"].index(stat_sort_choice)

        # sort the creatures list based on the selected stat
        sorted_creatures = sorted(creatures, key=lambda x: x[stat_index + 1], reverse=True)

        message = "Card name:\tStrength\tSpeed\tStealth\tCunning\n\n\n"

        # append each creature's stats to the message string
        for creature in sorted_creatures:
            message += f"{creature[0]}\t"
            for stat in creature[1:]:
                message += f"\t{stat}"
            message += "\n\n"

        # output the message using a message box in easygui
        easygui.msgbox(msg=message, title="Sorted Card Stats")

# main loop


while True:
    # display a choice box with the available options
    choice = easygui.buttonbox("Options", "Configuration Menu",
                               ("Storage", "Add", "Remove", "Edit", "Search", "Exit"))

    # execute the corresponding function based on the user's choice
    if choice == "Storage":
        display_card_stats()
    elif choice == "Add":
        add_card()
    elif choice == "Remove":
        remove_card()
    elif choice == "Edit":
        edit_card()
    elif choice == "Search":
        search_card()
    elif choice == "Exit":
        break
