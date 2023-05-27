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
        # create an interface for user to enter the name and stats of the new card
        while True:
            new_creature = easygui.enterbox("Enter the name and stats of the new card, separated by commas in order "
                                            "(e.g. 'Name, Str, Spe, Ste, Cun'):")

            if new_creature is None:
                # user clicked cancel, return to main menu
                break

            # split the input string into name and stats
            name_and_stats = new_creature.split(",")
            if len(name_and_stats) < 5:  # check if user provided all 5 stats
                easygui.msgbox("Please enter ALL stats")
            elif len(name_and_stats) > 5:  # check if user provided 5 stats
                easygui.msgbox("Please enter ONLY 5 stats")
            else:
                name, str_, spe, ste, cun = [s.strip() for s in name_and_stats]  # unpack the stats
                # validate the stats
                try:
                    str_, spe, ste, cun = map(int, (str_, spe, ste, cun))
                    if not all(0 <= stat <= 25 for stat in (str_, spe, ste, cun)):
                        easygui.msgbox("Invalid Stats: Stats must be integers between 0 and 25")
                    else:
                        # add the new creature to the list
                        creatures.append([name, str_, spe, ste, cun])
                        easygui.msgbox(f"Added {name} to the card list!")
                        break
                except ValueError:
                    easygui.msgbox("Invalid Stats: Stats must be integers between 0 and 25")

    elif choice == "Remove":
        # create an interface for user to enter the name of the card they want to remove
        card_name = easygui.enterbox("Enter the name of the card you want to remove:")

        if card_name is None:
            easygui.msgbox("Invalid Card name")
        elif card_name not in creatures:
            easygui.msgbox(f"Successfully removed {card_name} from the card list!")

        # find the card in the list and remove it
        for creature in creatures:
            if creature[0] == card_name:
                creatures.remove(creature)
                break
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