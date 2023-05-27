import easygui
from Dic import creatures


def add_card():
    card_name = easygui.enterbox("Enter the card name:")

    if not card_name:
        return  # User canceled, do nothing

    strength = easygui.enterbox(f"\tEnter the new strength value for '{card_name}':"
                                "\nValue must be higher or equal to than 0 and lower or equal to 25")
    if strength is None:
        easygui.msgbox("Editing canceled for creature: " + card_name)
        return
    if not strength:
        return

    speed = easygui.enterbox(f"\tEnter the new speed value for '{card_name}':"
                             "\nValue must be higher or equal to than 0 and lower or equal to 25")
    if speed is None:
        easygui.msgbox("Editing canceled for creature: " + card_name)
        return
    if not speed:
        return

    stealth = easygui.enterbox(f"\tEnter the new stealth value for '{card_name}':"
                               "\nValue must be higher or equal to than 0 and lower or equal to 25")
    if stealth is None:
        easygui.msgbox("Editing canceled for creature: " + card_name)
        return
    if not stealth:
        return

    cunning = easygui.enterbox(f"\tEnter the new cunning value for '{card_name}':"
                               "\nValue must be higher or equal to than 0 and lower or equal to 25")
    if cunning is None:
        easygui.msgbox("Editing canceled for creature: " + card_name)
        return
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

add_card()