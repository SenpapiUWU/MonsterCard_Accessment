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
            display_card_stats()
        else:
            easygui.msgbox("Card removal canceled.")


display_card_stats()
remove_card()
