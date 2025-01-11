from random import randint
from dataclasses import dataclass
from termcolor import colored
from typing import List

from Combatter import Combatter
from ..Item import Item
from ..Tags import *

"""
Pet needs to be reworked to be a subclass of Character.
"""


# A pet is an entity which will have its own
# turns just like any character. It will also
# be able to attack (melee or distance) and
# to position itself
# A pet can position itself either in front,
# next or back of the character.
# A pet in front will receive all damage until it faints
# A pet placed next to the character will behave just like
# any character
# A pet placed behind will not take any damage from melee attacks 
class Pet(Item):
    LIFE_PER_LEVEL:int
    DAMAGE_PER_LEVEL:int
    PROTECTION_PER_LEVEL:int
    
    MIN_SPEED:int
    MAX_SPEED:int

    MIN_ATTACKSPEED:int
    MAX_ATTACKSPEED:int

    MIN_EVASION:int=0
    MAX_EVASION:int=20

    MIN_PRECISSION:int=80
    MAX_PRECISSION:int=100

    tags = {PET}
    level:int
    name:int
    strength:int
    life:int
    speed:int
    attack_speed:int
    attack_form:str
    protection:int
    precission:int
    evasion:int
    positioning:str
    types:List

    attributes:"Pet_attr"

    max_equiped_armor:int=0

    _position_beautify = {"back":"behind", "next":"next to", "front":"in front of"}

    combats_played:int=0

    def __init__(self, owner, level:int, life:int=None, strength:int=None, protection:int=None):
        self.owner = owner

        self.name = f"{self.owner.name}'s {self.name}"

        self.level = (level if randint(0,10) else level + 1 if randint(0,1) else level -1) or 1

        self.life = (self.LIFE_PER_LEVEL*level + randint(0, self.LIFE_PER_LEVEL)
                    if life is None else life)

        self.strength = (self.DAMAGE_PER_LEVEL*level + randint(0, self.DAMAGE_PER_LEVEL)
                    if strength is None else strength)

        self.protection = (self.PROTECTION_PER_LEVEL*level + randint(0, self.PROTECTION_PER_LEVEL)
                    if protection is None else protection)

        self.speed = randint(self.MIN_SPEED, self.MAX_SPEED)

        self.attack_speed = randint(self.MIN_ATTACKSPEED, self.MIN_ATTACKSPEED)

        self.evasion = randint(self.MIN_EVASION, self.MAX_EVASION)

        self.precission = randint(self.MIN_PRECISSION, self.MAX_PRECISSION)

        self.equiped_armor = []

    def __str__(self):
        return f"Pet {self.name} ({self.attack_form}) (lvl: {self.level})"

    def call(self, combatter, turn):
        if(self in combatter.called_items):
            return

        self.attributes = Pet_attr(self.strength, self.life, self.speed, 
                    self.attack_speed, self.attack_form, self.precission,
                    self.evasion, self.protection, combatter)

        self.positioning = self.new_positioning()
        combatter = Combatter_pet(combatter.combat, self, combatter.team_index, 
                                    combatter.team_name, turn)

        if(not combatter.add_pet(combatter, self.positioning)): return

        print(f"{self.name} has been called to battle!")
        print(f"{self.name} placed itself {self._position_beautify[self.positioning]} {self.owner.name}")

        combatter.combat.attack_order.append(combatter)

    def share(self):
        result = {}

        for attr in list(dir(self))[::-1]:
            if(attr.startswith('_')):
                break
            elif(not callable(self.__getattribute__(attr))):
                result[attr] = self.__getattribute__(attr)

        return result

    def get_xp(self, xp):
        pass

    def end_combat(self, *args):
        self.combats_played += 1
    
    # Auxiliar

    def new_positioning(self):
        return self.positioning

    # Properties
    #@property
    #def _life(self) -> str:
    #    color_index = int(self.attributes.life*(len(self.life_colors)-1)/self.life)
    #    return colored(int(self.attributes.life), self.life_colors[0 if color_index < 0 else color_index])

class Combatter_pet(Combatter):
    positioning:str
    callables:list = []
    attacks:list = []

    def __init__(self, combat, pet, team_index, team_name, turn):
        self.positioning = pet.positioning
        self.turn = turn

        max_equiped_armor:int = min(pet.max_equiped_armor, combat.MAX_EQUIPED_ARMOR)
        equiped_armor = {}

        super().__init__(combat, pet, team_index, team_name, is_companion=True)

    def attack(self, enemy:"Combatter", *, can_call=None):
        if(randint(0,100) < self.attributes.precission and 
                randint(0,100) > enemy.attributes.evasion):
            print(f"{self.name} attacked {enemy.name}!")

            enemy.receive_hit(self.attributes.strength, self, None, self.attack_form)
        else:
            print(f"{self.name} missed its attempt to attack!")

    def receive_hit(self, damage:int, attacker:"Combatter", attack_to:"Armor"=None, attack_form:str="melee"):
        print(f"{self.name} received a direct hit! "
                            f"({self.life}hp -> ",end='')
        self.attributes.life -= (damage*((1/self.attributes.defense 
                                        if attack_form != "magic" else 1)))*(1+randint(0,10)/10)
        print(self.life, end='hp )\n')

        if(self.attributes.life <= 0):
            self.die()

    def die(self):
        print(f"{self.name} ({self.positioning}) fainted!")

        if(self.positioning != "next"):
            self.attributes.combatter.pets[self.positioning].remove(self)
        else:
            if(len(self.combat.participants[self.team_name]) > 1):
                print(self.combat.participants[self.team_name])
                self.combat.participants[self.team_name].remove(self)
            else:
                del self.combat.participants[self.team_name]

        self.is_alive = False
        self.attributes.combatter.called_items.append(self)

@dataclass
class Pet_attr():
    strength:int
    life:int
    speed:int
    attack_speed:int
    attack_form:str
    precission:int
    evasion:int
    defense:int
    combatter:"Combatter"=None
    stun:int=0

"""
@dataclass
class Dummy(Pet):
    LIFE_PER_LEVEL:int
    DAMAGE_PER_LEVEL:int
    PROTECTION_PER_LEVEL:int
    
    MIN_SPEED:int
    MAX_SPEED:int

    MIN_ATTACKSPEED:int
    MAX_ATTACKSPEED:int

    MIN_EVASION:int
    MAX_EVASION:int

    MIN_PRECISSION:int
    MAX_PRECISSION:int

    level:int
    name:int
    strength:int
    life:int
    speed:int
    attack_speed:int
    attack_form:str
    protection:int
    precission:int
    evasion:int
    positioning:str

    attributes:"Pet_attr"

    max_equiped_armor:int=0

    combats_played:int=0
    
    def __hash__(self):
        return super().__hash__()
"""