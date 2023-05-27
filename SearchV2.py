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


display_card_stats()

stat_choice = easygui.buttonbox("Please select search options", "Search Options",
                                        ["Sort by stats", "Search by name", "Cancel"])

while True:
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

    break
