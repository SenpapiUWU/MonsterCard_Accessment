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


while True:
    # display a choice box with the available options
    choice = easygui.buttonbox("Options", "Configuration Menu",
                               ("Storage", "Add", "Remove", "Edit", "Search", "Exit"))

    # execute the corresponding function based on the user's choice
    if choice == "Storage":
        display_card_stats()
    elif choice == "Edit":
        edit_card()
    elif choice == "Exit":
        break

