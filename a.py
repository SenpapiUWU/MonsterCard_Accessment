import easygui

creatures = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmiraj": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolm": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

# make the code keep going if there is no issue
while True:
    message = "Creature\t\tStrength\tSpeed\tStealth\tCunning\n\n\n"

    for creature, stats in creatures.items():
        message += f"{creature}\t"
        for stat in stats.values():
            message += f"\t{stat}"
        message += "\n\n"

    easygui.msgbox(msg=message, title="Card Stats")

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
