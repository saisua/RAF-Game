from random import randint
from typing import Any

from .Ability import Ability, Effect

class Defense(Ability):
    MAX_TURNS = 4
    MIN_EFFECT = 1
    MAX_EFFECT = 5 # * 1.value

    name:str="defense boost"
    turns:int

    effect:Effect
    effectiveness:float

    previous_value:Any

    #name:str, functions:Iterable[function], args:Iterable[dict], 
    #                    start:function=None, end:function=None, turns:int=1):
    def __init__(self, owner:"Character", level:int=1, turns=None, groupal=None):
        self.effectiveness = 1 + (randint(self.MIN_EFFECT,self.MAX_EFFECT)/10)

        super().__init__(owner=owner, turns=turns, groupal=groupal)

        self.effect = Effect(self.name, [], None, self.start, self.end, self.turns)

    def start(self, combatter):
        print(f"{self.owner.name} used Ability {self.name}"
                    f"{'' if combatter == self.owner else f' to {combatter.name}'}!")
        self.previous_value = combatter.attributes.defense
        
        combatter.attributes.defense *= self.effectiveness

    def end(self, combatter):
        print(f"{self.name} has ended in {combatter.name}")
        combatter.attributes.defense = self.previous_value