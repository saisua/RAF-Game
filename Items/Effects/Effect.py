from typing import Iterable 
from itertools import cycle

from ..Item import Item
from ..Tags import *

# In theory the class effect should be good enough
# to do almost anything. Children classes will
# exist mostly to keep things rather tidy
class Effect(Item):
    name:str
    effect_name:str
    functions:cycle
    args:cycle
    turns:int
    end:callable

    tag = {EFFECT, OVER_TIME}
    started:bool=False

    descriptions:cycle

    def __init__(self, functions:Iterable[callable]=[], args:Iterable[dict]=[{}],
                    descriptions:Iterable[callable]=[{}]):
        if(len(functions) or functions is not None and len(self.functions)):
            self.functions = cycle(functions)
            self.args = cycle(args)
            self.descriptions = cycle(descriptions)

    def apply(self, combatter):
        self.turns -= 1

        if(not self.started):
            if(self.on_start):
                self.on_start(combatter)

                self.started = True
                return True
            self.started = True

        if(self.turns >= 0):
            if(self.functions_length):
                return True
        else:
            if(self.end):
                self.end(combatter)
            
            combatter.effects.remove(self)

            return False

    def on_start(self, combatter, **kwargs):
        print(f"{combatter.name} got {self.effect_name}!")
        self.on_turn(combatter)

    def on_turn(self, combatter, **kwargs): 
        if(len(self.functions)):
            next(self.functions)(**{"combatter":combatter, **next(self.args),  **kwargs})
            print(next(self.descriptions))

    def on_end(self, combatter, **kwargs):
        pass
