from random import randint

from .Ability import Ability
from ..Tags import *

class Double_turn(Ability):
    tags:set = (Ability.tags |
            {DEFENSIVE, MULTI_TARGET,
            STATUS}
        )
    name:str="double turn"
    turns:int

    effectiveness:float

    #name:str, functions:Iterable[function], args:Iterable[dict], 
    #                    start:function=None, end:function=None, turns:int=1):
    def __init__(self, owner:"Character"=None, level:int=1, turns=None, groupal=None):
        super().__init__(owner=owner, turns=0, groupal=False)


    def call(self, combatter, _=None):
        print(f"{self.owner.name} used Ability {self.name}!")
        combatter.combat.attack_order.insert(0, combatter)
