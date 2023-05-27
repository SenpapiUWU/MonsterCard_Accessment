import easygui
from Dic import creatures

card_name = easygui.enterbox("Enter the card name:")
if card_name:
    strength = easygui.enterbox("Enter the strength value:")
    speed = easygui.enterbox("Enter the speed value:")
    stealth = easygui.enterbox("Enter the stealth value:")
    cunning = easygui.enterbox("Enter the cunning value:")

    creatures.append([card_name, strength, speed, stealth, cunning])
