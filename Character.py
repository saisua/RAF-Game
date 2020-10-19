from collections import defaultdict
from dataclasses import dataclass
from random import choice, randint
from codecs import encode, decode
from os.path import isfile
from operator import add
import dill
import zlib
import datetime

from character.attributes import Attr_creation

from Items.Random_item import Random_item, _groups as items_dict#, items_dummies

from Items.Armors.Random_armor import Random_armor as Armor, armor_types
from Items.Armors.Shoes import Shoes

from Items.Pets.Random_pet import Random_pet as Pet
from Items.Pets.Cat import Cat

from Items.Spells.Random_spell import Random_spell as Spell

from Items.Weapons.Random_weapon import Random_weapon as Weapon
from Items.Weapons.Random_weapon import Random_melee_weapon as Melee_weapon
from Items.Weapons.Random_weapon import Random_distance_weapon as Distance_weapon
from Items.Weapons.Dagger import Dagger
from Items.Weapons.Spear import Spear
from Items.Weapons.Nunchakus import Nunchakus
from Items.Weapons.Hammer import Hammer

from Items.Abilities.Random_ability import Random_ability as Ability


class Character():
    _EXPERIENCE_PER_LEVEL:int = 60
    _COMBATS_PER_ITEM:int = 6
    _MAX_COMBATS_A_DAY:int = 5
    _ADD_COMBAT_EVERY_LEVEL:int = 5

    name:str
    level:int
    experience:int
    combats_played:int
    attributes:"Attributes"
    items:defaultdict

    max_held_items:int
    max_equiped_armor:int
    max_pets_front:int = 100
    max_pets_back:int = 100

    last_combat:"datetime" = datetime.datetime.now()
    today_combats:int=0

    _last_code:str=None
    
    def __init__(self, name:str, level:int=1, max_held_items:int=1):
        self.name = name
        self.attributes, maximums = Attr_creation.create()
        self.items = {i_name:{specific:[] for specific in item.keys()} for i_name,item in items_dict.items()}
        self.max_held_items = max_held_items
        self.max_equiped_armor = armor_types

        self.level = level
        for _ in range(level-1):
            self.level_up()

        self.experience = 0
        self.combats_played = 0

        print(f"Welcome, {name} {self.attributes.description}")

        
        for item in maximums:
            type_, class_ = {"evasion" : ["Pet", Cat],
            "precission" : ["Weapon", Distance_weapon],
            "strength" : ["Weapon", Melee_weapon],
            "speed" : ["Armor", Shoes],
            "attack_speed" : ["Weapon", Dagger],
            "knock" : ["Weapon", Nunchakus],
            "stun" : ["Weapon", Weapon],
            "weapon_rate" : ["Weapon", Weapon],
            "weapon_strength" : ["Weapon", Hammer],
            "magic" : ["Spell", Spell],
            "magic_strength" : ["Spell", Spell],
            "defense" : ["Armor", Armor],
            "pet_rate" : ["Pet", Pet],
            "life" : ["Armor", Armor],
            "magic_defense" : ["Armor", Armor],
            "ability_rate" : ["Ability", Ability]}[item]

            if(not type_ is None):
                new_item = class_(self)

                print(f"  You received a new {new_item}!")
                self.items[type_][new_item.__class__.__name__].append(new_item)
        

    def __str__(self) -> str:
        return f"{self.name} {self.attributes.description} (lvl: {self.level})"

    @property
    def _item_stats(self) -> str:
        items_print = []
        for type_name, sub_types in self.items.items():
            items_print.append(f"\n\t{type_name}s:")
            for sub_type, elements in sub_types.items():
                items_print.append(f"\n\t\t{sub_type}:")
                for element in elements:
                    items_print.append(f"\n\t\t\t{str(element)}")
        
        return f"{self.name} {self.attributes.description} (lvl: {self.level}) \n  Items held: {''.join(items_print)}"



    def add_item(self, item):
        print(f"  {self.name} received a new {item}!")
        self.items[item.__class__.__bases__[0].__name__][item.__class__.__name__].append(item)

    def get_xp(self, xp:int):
        print(f"{self} got {xp}xp", end='')
        self.experience += xp

        if(self.experience >= self._EXPERIENCE_PER_LEVEL*self.level):
            self.level += 1
            self.experience = 0

            self.level_up()

            print(f"!\n{self} leveled up to level {self.level}! "+choice(
                ["Nice job!", "Congratulations!", "As expected", "Well done!",
                "Keep it going!"]
            ))
        else:
            print(f" -> {self.experience}xp!")

    def end_combat(self, combat_datetime:"datetime"):
        self.combats_played += 1

        if(not self.combats_played % self._COMBATS_PER_ITEM):
            self.add_item(Random_item(self))

        if(self.last_combat.date() < combat_datetime.date()):
            self.today_combats = 1
        else:
            self.today_combats += 1
        
        self.last_combat = combat_datetime

    def level_up(self):
        # The amount of points are based on the difference
        # Between attributes.profile_value to 0.5
        # Plus minus random amount of points
        # Points are allocated randomly

        # profile_value is based in the max amount of points
        # can have any player based on the level
        # (not taking in account random plus points)

        multiplier = ((1-self.attributes.profile_value)+0.5)**2
        new_profile_value = 0

        #print(f"\n[debug] profile_value = {self.attributes.profile_value}\n")

        for attr, max_value in Attr_creation.level_up.items():
            min_value = (max_value*(self.level-1))-self.attributes._get(attr)
            add_value = True

            if(min_value < 0):
                if(randint(0,1)):
                    min_value = -max_value*2 // 3
                else:
                    add_value = 0
            else:
                min_value = min_value // 2

            add_value = add_value and randint(min_value, min_value+max_value)*multiplier

            #print(f"add_value: {add_value}")

            # Keep attributes around a level-based maxim
            adjust_value = add_value + self.attributes._get(attr)
            if(adjust_value > max_value*self.level):
                #print("Value was to be too big")
                reduction_value = 1-(adjust_value/(max_value*self.level))
                adjust_value = reduction_value if 0 < reduction_value < 1 else 0.1
            else: 
                adjust_value = 1
            #print(f"[debug] {attr}   {self.attributes._get(attr)} -> ",end='')

            #print(f"adjust_value: {adjust_value}")
            self.attributes._set(attr, add_value*adjust_value, add)
            new_profile_value += self.attributes._get(attr)/(max_value*self.level)

            #print(self.attributes._get(attr))

        self.attributes.profile_value = new_profile_value/len(Attr_creation.level_up)
        #print(f"\n[debug] new profile_value = {self.attributes.profile_value}\n")

    def share(self):
        result = {}

        for attr in list(dir(self))[::-1]:
            if(attr.startswith('_')):
                break
            elif(not callable(self.__getattribute__(attr))):
                result[attr] = self.__getattribute__(attr)

        """
        result_items = {}
        for type_,items in self.items.items():
            result_items[type_] = {}
            for item_name,item_list in items.items():
                result_items[type_][item_name] = []

                for item in item_list:
                    result_items[type_][item_name].append(item.share())

        result["items"] = result_items
        """

        return result

    def save(self, file_name:str=None):
        if(file_name is None):
            file_name = self.name

        print(f"Saving character {self}... ", end='')
        with open(file_name+".chr", 'wb') as file:
            file.write(encode(zlib.compress(dill.dumps(self.share())), "base_64"))
        print("DONE")
    
    # Properties


    @property
    def _stats(self) -> str:
        print(dict(self.attributes))

    @property
    def _can_play(self) -> bool:
        if(self.last_combat.date() < datetime.date.today()):
            self.today_combats = 0
        elif(self.today_combats >= 
                (self._MAX_COMBATS_A_DAY + self.level // self._ADD_COMBAT_EVERY_LEVEL)):
            return False

        return True

    # Static functions

    @staticmethod
    def load(file_name:str):
        if(not isfile(file_name+".chr")):
            return None

        with open(file_name+".chr", "rb") as file:
            loaded = Dummy(**dill.loads(zlib.decompress(decode(file.read(), "base_64"))))
        #loaded._load()

        loaded._can_play

        print(f"Welcome again, {loaded}  -  (played combats today: {loaded.today_combats})")
        return loaded

@dataclass
class Dummy(Character):
    name:str
    level:int
    experience:int
    combats_played:int
    attributes:"Attributes"
    items:defaultdict

    max_held_items:int
    max_equiped_armor:int
    max_pets_front:int = 100
    max_pets_back:int = 100

    last_combat:"datetime" = datetime.datetime.now()
    today_combats:int=0

    """
    def _load(self):
        result_items = defaultdict(lambda: defaultdict(list))
        for type_,items in self.items.items():
            for item_name,item_list in items.items():
                for item in item_list:
                    result_items[type_][item_name].append(items_dummies[type_](**item))

        self.items = result_items
    """
    
    def __hash__(self):
        return super().__hash__()