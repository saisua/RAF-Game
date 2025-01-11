from random import randint
from typing import List

from .Ability import Ability
from ..Tags import *

class Magic(Ability):
    PROB_GROUPAL = 0
    MAX_TURNS = 3
    MIN_EFFECT = 15
    MAX_EFFECT = 30

    tags = (Ability.tags |
            {RECOVER}
        )
    name:str="magic recover"
    turns:int
    types:List

    effectiveness:float

    #name:str, functions:Iterable[function], args:Iterable[dict], 
    #                    start:function=None, end:function=None, turns:int=1):
    def __init__(self, owner:"Character"=None, level:int=1, turns=None, groupal=None):
        super().__init__(owner=owner, turns=0, groupal=groupal)

        self.effectiveness = (randint(self.MIN_EFFECT,self.MAX_EFFECT/2 if self.groupal else self.MAX_EFFECT))

    def call(self, combatter, _=None):
        print(f"{self.owner.name} used Ability {'groupal' if self.groupal else ''} {self.name}!")

        if(self.groupal):
            apply_to = combatter.combat.participants[combatter.team_name]
        else:
            apply_to = [combatter]

        for combatter in apply_to:
            if(combatter._static.__class__.__name__ == "Pet"): continue
            print(f"{combatter.name} recovers some magic ({combatter.magic}mp -> ",end='')
            magic_cap = combatter._static.attributes.magic - combatter.attributes.magic
            combatter.attributes.magic += self.effectiveness if self.effectiveness < magic_cap else magic_cap
            print(f"{combatter.magic}mp)")
