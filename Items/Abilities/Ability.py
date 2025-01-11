from random import randint
from copy import deepcopy
from dataclasses import dataclass
from typing import List

from ..Effects.Effect import Effect
from Types.Type import Type
from ..Item import Item,
from ..Tags import *

class Ability(Item):
    PROB_GROUPAL:int = 7 # 1/value
    MAX_TURNS:int

    tags = {ABIILITY}
    owner:"Character"
    name:str
    groupal:bool
    turns:int
    types:List[str]

    effect:Effect

    def __init__(self, owner:"Character"=None, level:int=1, turns:int=None, name:str=None, groupal:bool=None):
        self.owner = owner
        
        if(name): self.name = name

        self.turns = randint(1, self.MAX_TURNS) if turns is None else turns
        self.groupal = not bool(randint(0,self.PROB_GROUPAL))

    def __str__(self):
        return f"{'groupal ' if self.groupal else ''}ability ({self.name})"

    def call(self, combatter:"Combatter", _=None):
        if(self.groupal):
            apply_to = combatter.combat.participants[combatter.team_name]
        else:
            apply_to = [combatter]

        for combatter in apply_to:
            combatter.add_effect(deepcopy(self.effect))

    def start(self, combatter):
        pass

    def end(self, combatter):
        pass

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
class Dummy(Ability):
    PROB_GROUPAL:int
    MAX_TURNS:int

    owner:"Character"
    name:str
    groupal:bool
    turns:int

    effect:Effect
    
    def __hash__(self):
        return super().__hash__()
"""