from typing import Iterable 
from itertools import cycle

# In theory the class effect should be good enough
# to do almost anything. Children classes will
# exist mostly to keep things rather tidy
class Effect():
    name:str
    functions:cycle
    args:cycle
    turns:int
    end:callable

    started:bool=False
    functions_length:int

    descriptions:cycle

    def __init__(self, name:str, functions:Iterable[callable]=[], args:Iterable[dict]=[{}], 
                        start:callable=None, end:callable=None, turns:int=1):
        self.name = name
        self.functions_length = bool(len(functions))
        self.functions = cycle(functions)
        if(args and self.functions_length): self.args = cycle(args)
        self.turns = turns
        self.start = start
        self.end = end

    def apply(self, combatter):
        self.turns -= 1

        if(not self.started):
            if(self.start):
                self.start(combatter)

                self.started = True
                return True
            self.started = True

        if(self.turns >= 0):
            if(self.functions_length):
                (next(self.functions) or (lambda **kwargs:0))(**{"combatter":combatter, **next(self.args)})
                return True
        else:
            if(self.end):
                self.end(combatter)
            
            combatter.effects.remove(self)

            return False        