import easygui
from Dic import creatures
# make the rows for each category
message = "Creature\t\tStrength\tSpeed\tStealth\tCunning\n\n\n"

# loop through the creatures dictionary and append each creature's stats to the message string
for creature in creatures:
    message += f"{creature[0]}\t"
    for stat in creature[1:]:
        message += f"\t{stat}"
    message += "\n\n"
# output the message using a message box in easygui
while True:
    easygui.msgbox(msg=message, title="Creature Stats")
    choice = easygui.buttonbox("Option", "Config Menu", ("Add", "Remove", "Storage", "Exit"))
    # create storage choice
    if choice == "Storage":
        pass
    # create Remove choice
    elif choice == "Remove":
        card_name = easygui.enterbox("Enter the name of the card you want to remove:")
        pass
# create Add interface
    elif choice == "Add":
        # add different section for each info
        card_name = easygui.enterbox("Enter the name of the new card:")
        strength = easygui.enterbox("Enter the strength value:")
        speed = easygui.enterbox("Enter the speed value:")
        stealth = easygui.enterbox("Enter the stealth value:")
        cunning = easygui.enterbox("Enter the cunning value:")
    else:
        break
