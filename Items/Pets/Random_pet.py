from random import choice

from .Dog import Dog
from .Cat import Cat
from .Dragon import Dragon
from .Spider import Spider
from .Turtle import Turtle

_by_name = {
    "Dog":Dog, 
    "Cat":Cat, 
    "Dragon":Dragon, 
    "Spider":Spider, 
    "Turtle":Turtle
}

def Random_pet(owner:"Character", name:str=None):
    return _by_name.get(name, choice(list(_by_name.values()))
            )(owner, owner.level)
