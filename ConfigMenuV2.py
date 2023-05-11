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
        #  create an interface for user to enter the name and stats of the new card
        new_creature = easygui.enterbox("Enter the name and stats of the new card,"
                                        " separated by commas in order (e.g. 'Name, Str, Spe, Ste, Cun'):")

        # add the new card info from user to the list
        new_creature = new_creature.split(",")
        new_creature[1:] = [int(stat) for stat in new_creature[1:]]
        creatures.append(new_creature)
        # allow user to remove the card from storage
    elif choice == "Remove":
        pass
    # Return user to the card storage
    elif choice == "Storage":
        pass

    else:
        break
