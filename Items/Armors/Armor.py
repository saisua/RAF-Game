from random import randint
from dataclasses import dataclass
from typing import List

from .. import Item
from ..Tags import *

# Any attack will target one of the armor-sitting zones
# In case of hit, it will hit the armor, reducing the damage
# dealt.
class Armor(Item):
    LIFE_PER_LEVEL:int
    PROTECTION_PER_LEVEL:int
    DAMAGE_PART:float

    tags = {ARMOR, DEFENSIVE}
    level:int=None
    name:int=None
    protection:int=None
    life:int=None
    quality:str=None
    types:List

    _qualities = ["Bad", "Regular", "Good", "Excellent"]

    def __init__(self, owner=None, level:int=1, life:int=None, protection:int=None):
        self.owner = owner

        self.level = (level if randint(0,10) else level + 1 if randint(0,1) else level -1) or 1

        self.life = (self.LIFE_PER_LEVEL*level + randint(0, self.LIFE_PER_LEVEL)
                    if life is None else life)

        self.protection = (self.PROTECTION_PER_LEVEL*level + randint(0, self.PROTECTION_PER_LEVEL)
                    if protection is None else protection)

        self.quality = self._qualities[int((self.life%self.LIFE_PER_LEVEL + self.protection%self.PROTECTION_PER_LEVEL)
                        * (len(self._qualities)-1)
                        / (self.LIFE_PER_LEVEL+self.PROTECTION_PER_LEVEL))]

    def __str__(self):
        return f"Level {self.level} {self.name} of quality: {self.quality}"

    def receive_hit(self, combatter, damage:float, attacker, after:str='') -> str:
        real_damage = damage * 1/self.protection

        combatter.attributes.life -= real_damage
        self.life -= real_damage

        if(self.life <= 0):
            self.owner.items["Armor"][self.__class__.__name__].remove(self)
            del combatter.equiped_armor[self.__class__.__name__]

            return f"The {self.name} broke off after absorbing {damage-real_damage} damage"+after

        return f"The {self.name} absorbed {int(damage-real_damage)} damage"+after

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
class Dummy(Armor):
    LIFE_PER_LEVEL:int
    PROTECTION_PER_LEVEL:int
    DAMAGE_PART:float

    level:int=None
    name:int=None
    protection:int=None
    life:int=None
    quality:str=None
    
    def __hash__(self):
        return super().__hash__()
"""