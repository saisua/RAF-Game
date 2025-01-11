from random import randint
from dataclasses import dataclass
from typing import List

from ..Item import Item
from ..Tags import *

class Weapon(Item):
    LIFE_PER_LEVEL:int
    DAMAGE_PER_LEVEL:int

    MAX_TARGETS:int

    MAX_CHARGES:int

    MAX_HITS:int=1

    tags = {WEAPON, OFFENSIVE}
    level:int=None
    name:int=None
    damage:int=None
    life:int=None
    attack_form:str=None
    targets:int=None
    reload_turns:int=None
    charges:int=None
    quality:str
    types:List

    reloading:int = 0

    _qualities = ["nicked","harmful","blood-soaked"]

    def __init__(self, owner:"Character"=None, level:int=1, damage:int=None, life:int=None,
                    targets:int=None, charges:int=None):
        self.owner = owner

        self.level = (level if randint(0,10) else level + 1 if randint(0,1) else level -1) or 1

        self.life = (self.LIFE_PER_LEVEL*level + randint(0, self.LIFE_PER_LEVEL)
                    if life is None else life)

        self.damage = (self.DAMAGE_PER_LEVEL*level + randint(0, self.DAMAGE_PER_LEVEL)
                    if damage is None else damage)

        self.targets = (randint(1, self.MAX_TARGETS) if targets is None else targets)

        self.charges = randint(1, self.MAX_CHARGES) if charges is None else charges

        self.quality = self._qualities[int(self.damage%self.DAMAGE_PER_LEVEL 
                * len(self._qualities)
                / self.DAMAGE_PER_LEVEL)]

    def __str__(self):
        return f"{self.quality} {self.name}"

    def call(self, combatter, _):
        if(len(combatter.held_items) < combatter.max_held_items and not self in combatter.called_items):
            print(f"{self.owner.name} picked up a {self.name}!")
            self.charges = randint(int(self.MAX_CHARGES/2), self.MAX_CHARGES)

            combatter.held_items.append(self)

    def attack(self, enemy, attack_to, combatter):
        if(self.reloading):
            print(f"{self.owner.name} is reloading")
            self.reloading -= 1
            return

        for _ in range(1 if randint(0,10) else randint(1,self.MAX_HITS)):
            if(not enemy.is_alive): break
            print(f"{self.owner.name} attacked {enemy.name} using a {self.name}!")
            enemy.receive_hit(combatter.attributes.strength+self.damage, combatter, attack_to, self.attack_form)
            self.charges -= 1
            self.reloading = self.reload_turns

            self.life -= 10
            if(self.life <= 0):
                self.broke(combatter)
                return

            elif(self.charges <= 0):
                self.drop(combatter)
                return

    def broke(self, combatter):
        combatter.held_items.remove(self)
        print(f"{self.owner.name}'s {self.name} broke!")
        self.owner.items["Weapon"][self.__class__.__name__].remove(self)

    def drop(self, combatter, extra_message:str=''):
        combatter.held_items.remove(self)
        print(f"{self.owner.name} dropped the {self.name}{f' {extra_message}'}!")

        if(not combatter.combat.rules["reusing weapons"]):
            combatter.called_items.append(self)

    def share(self):
        result = {}

        for attr in list(dir(self))[::-1]:
            if(attr.startswith('_')):
                break
            elif(not callable(self.__getattribute__(attr))):
                result[attr] = self.__getattribute__(attr)

        return result

""" 
@dataclass
class Dummy(Spell):
    LIFE_PER_LEVEL:int
    DAMAGE_PER_LEVEL:int

    MAX_TARGETS:int

    MAX_CHARGES:int

    MAX_HITS:int=1

    level:int=None
    name:int=None
    damage:int=None
    life:int=None
    attack_form:str=None
    targets:int=None
    reload_turns:int=None
    charges:int=None
    quality:str=''

    reloading:int = 0

    def __hash__(self):
        return super().__hash__()
"""