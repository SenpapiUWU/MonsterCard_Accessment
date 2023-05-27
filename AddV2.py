import easygui
from Dic import creatures

while True:
        new_creature = easygui.enterbox("Enter the name and stats of the new card, separated by commas in order "
                                        "(e.g. 'Name, Str, Spe, Ste, Cun'):")
        if new_creature is None:
            break
        name_and_stats = new_creature.split(",")
        if len(name_and_stats) < 5:
            easygui.msgbox("Please enter ALL stats")
        elif len(name_and_stats) > 5:
            easygui.msgbox("Please enter ONLY 5 stats")
        else:
            name, str_, spe, ste, cun = [s.strip() for s in name_and_stats]
            try:
                str_, spe, ste, cun = map(int, (str_, spe, ste, cun))
                if not all(0 <= stat <= 25 for stat in (str_, spe, ste, cun)):
                    easygui.msgbox("Invalid Stats: Stats must be integers between 0 and 25")
                else:
                    creatures.append([name, str_, spe, ste, cun])
                    easygui.msgbox(f"Added {name} to the card list!")
                    break
            except ValueError:
                easygui.msgbox("Invalid Stats: Stats must be integers between 0 and 25")
