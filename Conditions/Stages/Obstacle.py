from typing import Tuple
from dataclasses import dataclass

@dataclass
class Obstacle():
    name:str
    # random, border, points, center, across
    obstacle_type:str
    
    size:Tuple[int,int,int]
    size_variation:Tuple[int,int,int]=(0,0,0)

    obstacles_nearby:Tuple[str]

    # Connected means a character cannot cross it
    # unless it has a jump higher than the height of
    # it, but it can't attack across it unless
    # it has height <= 0
    connected:bool

    destroyable:bool

    climbable:bool

    symbol:str
    color:str