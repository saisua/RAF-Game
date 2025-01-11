from random import randint

from Character import Character, Dummy
from Items.Armors.Random_armor import Random_armor as Armor
from Items.Pets.Random_pet import Random_pet as Pet
from Items.Weapons.Random_weapon import Random_weapon as Weapon
from Items.Spells.Random_spell import Random_spell as Spell
from Items.Random_item import Random_item as Item
from Items.Abilities.Random_ability import Random_ability as Ability

from Items.Armors.Random_armor import _by_name as armors
from Items.Weapons.Random_weapon import _by_name as weapons

from Combat import Combat

from utils.communication import list_online, share, get_character

def safe_load(name:str, ask:bool, new:bool, **kwargs):
    char = None
    if(not new):
        char = Character.load(name)
    if(not char):
        char = Character(name, **kwargs)
        print('\n')
        return char, False
    print('\n')
    return char, ask

def main():
    ITEMS_PER_PLAYER = 0

    existed = True

    new = False
    level = 1

    while(True):
        print()
        main, existed = safe_load("Main", existed, new, level=level)
        viic14,existed = safe_load("Buddy", existed, new, level=level)

        for _ in range(ITEMS_PER_PLAYER):
            main.add_item(Item(main))
            viic14.add_item(Spell(viic14))

        if(existed): break
        if(not 'n' in input("Press enter to start \n")): break

    menu = {
        '1':"Fight",
        '2':"Show player stats",

        '0':"Quit"
    }
    
    menu_funct = {
        '1' : lambda: Combat({'Bona gent':[main, viic14], "Mala gent":[Character("Enemy1", main.level-randint(0,1)), 
                                                        Character("Enemy2", viic14.level-randint(0,1))]
            }).start_auto(),
        '2' : lambda: print(f"{main._item_stats}\n\n{viic14._item_stats}"),

        '0' : lambda:0
    }

    pstr = '\n\t'.join([f"[{num}] {desc}" for num, desc in menu.items()])
    del menu

    try:
        move = input(f"Menu: \n\t{pstr}\n> ")
        while(move != '0'):
            menu_funct.get(move, lambda:print("Invalid opion. Please choose another one"))()

            move = input(f"\nMenu: \n\t{pstr}\n> ")

    except KeyboardInterrupt:
        if('n' in input("\nSave anyway? [y] ").lower()):
            exit(0)

    print()
    main.save()
    viic14.save()

if __name__ == "__main__":
    main()