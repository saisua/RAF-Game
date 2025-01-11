from random import randint
from typing import Any

from .Ability import Ability, Effect
from ..Tags import *

class Regenerate(Ability):
    MAX_TURNS = 5
    MIN_EFFECT = 10
    MAX_EFFECT = 20 

    tags = (Ability.tags |
            {DEFENSIVE, MULTI_TARGET, HEALING,
            OVER_TIME}
        )
    name:str="regeneration"
    turns:int

    effect:Effect
    effectiveness:float

    previous_value:Any

    #name:str, functions:Iterable[function], args:Iterable[dict], 
    #                    start:function=None, end:function=None, turns:int=1):
    def __init__(self, owner:"Character"=None, level:int=1, turns=None, groupal=None):
        self.effectiveness = 1 + (randint(self.MIN_EFFECT,self.MAX_EFFECT)/10)

        super().__init__(owner=owner, turns=turns, groupal=groupal)

        self.effect = Effect(self.name, [self.each_turn], [{}], self.start, self.end, self.turns)


    def each_turn(self, combatter):
        print(f"{combatter.name} recovered some health ({combatter.life} -> ", end='')
        life_cap = combatter._static.attributes.life - combatter.attributes.life
        combatter.attributes.life += self.effectiveness if self.effectiveness < life_cap else life_cap
        print(f"{combatter.life})")

    def start(self, combatter):
        print(f"{self.owner.name} used {self.name}")
        self.each_turn(combatter)

    def end(self, combatter):
        print(f"{self.name} has ended in {combatter.name}")