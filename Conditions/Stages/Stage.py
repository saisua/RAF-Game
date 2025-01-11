from typing import Tuple, Iterable

from .Obstacle import Obstacle

class Stage():
    name:str
    inside:bool

    size:Tuple[int, int]
    obstacles:Iterable[Obstacle]

    layout:Tuple[tuple[int]]

    def __init__(self):
        pass

        self.generate_layout()

    def prettify(self):
        pass

    def generate_layout(self, participants:int=2):
        
        if("random" in self.obstacles):
            pass
        elif("borders" in self.obstacles):
            pass
        elif("points" in self.obstacles):
            pass
        elif("center" in self.obstacles):
            pass
        elif("across" in self.obstacles):
            pass