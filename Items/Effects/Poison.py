from random import randint

from .Effect import Effect
from ..Tags import *

class Poison(Effect):
    name = "poison"
    effect_name = "poisoned"

    tags = (Effect.tags | 
            OFFENSIVE, STATUS, OVER_TIME
        )
    
    poison_damage:int
    turns:int

    POISON_MAX_DAMAGE:int = 10
    POISON_MIN_DAMAGE:int = 3

    POISON_MAX_TURNS:int = 5
    POISON_MIN_TURNS:int = 1

    def __init__(self, max_damage=None, min_damage=None, 
                        max_turns=None, min_turns=None):

        if(max_damage is not None):
            self.POISON_MAX_DAMAGE = max_damage

        if(min_damage is not None):
            self.POISON_MIN_DAMAGE = min_damage

        if(max_turns is not None):
            self.POISON_MAX_TURNS = max_turns

        if(min_turns is not None):
            self.POISON_MIN_TURNS = min_turns

        self.poison_damage = randint(
                self.POISON_MIN_DAMAGE, 
                self.POISON_MAX_DAMAGE
            )

        self.turns = randint(
                self.POISON_MIN_TURNS, 
                self.POISON_MAX_TURNS
            )


    def on_turn(self, combatter):
        print(f"{combatter.name} got hurt by poison ({combatter.life} -> ", end='')
        combatter.attributes.life -= self.poison_damage
        print(f"{combatter.life})")

    def end(self, combatter):
        print(f"{combatter.name} has recovered from the poison")