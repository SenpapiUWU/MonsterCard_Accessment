import easygui
from Dic import creatures

while True:
    message = "Creature\t\tStrength\tSpeed\tStealth\tCunning\n\n\n"

    for creature in creatures:
        message += f"{creature[0]}\t"
        for stat in creature[1:]:
            message += f"\t{stat}"
        message += "\n\n"

    easygui.msgbox(msg=message, title="Card Stats")

    choice = easygui.buttonbox("Option", "Config Menu", ("Add", "Remove", "Storage", "Exit"))

    if choice == "Add":
        pass

    elif choice == "Storage":
        # Add code for Storage option
        pass

    elif choice == "Remove":
        # Add code for Remove option
        pass

    elif choice == "Exit":
        break