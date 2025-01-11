from random import randint, choice
from dataclasses import dataclass
from typing import List

from ..Item import Item
from ..Tags import *

class Spell(Item):
    tags = {SPELL, RANGED, MAGICAL}
    MIN_DAMAGE:int
    MAX_DAMAGE:int

    MIN_MAGIC:int
    MAX_MAGIC:int

    MAX_TARGETS:int

    element:str
    damage:int
    magic:int
    targets:int
    attack_form:str
    quality:str
    types:List

    _qualities = ["Weak", "Medium", "Powerful"]

    def __init__(self, owner=None, damage=None, magic=None, targets:int=None, attack_form:str=None):
        self.owner = owner

        self.damage = (randint(self.MIN_DAMAGE, self.MAX_DAMAGE) 
                        if damage is None else damage)

        self.magic = (randint(self.MIN_MAGIC, self.MAX_MAGIC) 
                        if magic is None else magic)

        self.targets = randint(1, self.MAX_TARGETS) if targets is None else targets

        self.attack_form = (choice(["melee", "distance"]) 
                            if attack_form is None else attack_form)

        self.quality = self._qualities[int(((self.damage*self.targets)+
                        (self.MAX_MAGIC-self.magic-self.MIN_MAGIC))
                        * (len(self._qualities)-1)
                        / (1+self.MAX_DAMAGE*self.MAX_TARGETS+(self.MAX_MAGIC-self.MIN_MAGIC)))]

    def __str__(self):
        return f"{self.quality} {self.element} spell ({self.attack_form} to {self.targets} targets)"

    def attack(self, enemy, attack_to, combatter, after:str='', attack:bool=True, once:bool=True):
        if(once):
            print(f"{self.owner.name} used {self.element} spell to {'attack' if attack else ''} {enemy.name}! ({combatter.magic}mp -> ", end='')
        
            combatter.attributes.magic -= self.magic
            print(f"{combatter.magic}mp)")
            
        if(randint(0,100) < combatter.attributes.precission):
            if(attack):
                if(randint(0,100) > enemy.attributes.evasion):
                    enemy.receive_hit(self.damage+combatter.attributes.magic_strength, 
                            combatter, attack_to, "magic")
                else:
                    return False

            if(after):
                print(after)
            return True
        return False
    
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
    MIN_DAMAGE:int
    MAX_DAMAGE:int

    MIN_MAGIC:int
    MAX_MAGIC:int

    MAX_TARGETS:int

    element:str
    damage:int
    magic:int
    targets:int
    attack_form:str
    quality:str
    
    def __hash__(self):
        return super().__hash__()
"""