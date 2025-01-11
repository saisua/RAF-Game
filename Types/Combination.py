from typing import Set

"""
Animal
Dark
Death
Earth
Electric
Fire
Ice
Light
Plant
Poison
Water
Wind
"""

from .Type import Type
from .Animal import Animal
from .Dark import Dark
from .Death import Death
from .Earth import Earth
from .Electric import Electric
from .Fire import Fire
from .Ice import Ice
from .Light import Light
from .Plant import Plant
from .Poison import Poison
from .Water import Water
from .Wind import Wind

# The types from Combination must be generated when the
# required combinations of types occur
class Combination(Type):
    requirements:Set[Type]

    names:dict = {
        (Animal.flag & Dark.flag) : "Devil",
        (Animal.flag & Death.flag) : "Corpse",
        (Animal.flag & Earth.flag) : "",
        (Animal.flag & Electric.flag) : "Robot",
        (Animal.flag & Fire.flag) : "Phoenix",
        (Animal.flag & Ice.flag) : "",
        (Animal.flag & Light.flag) : "Angel",
        (Animal.flag & Plant.flag) : "Druidic",
        (Animal.flag & Poison.flag) : "Venom",
        (Animal.flag & Water.flag) : "Fish",
        (Animal.flag & Wind.flag) : "Bird",
        (Dark.flag & Death.flag) : "Dark magic",
        (Dark.flag & Earth.flag) : "Dust",
        (Dark.flag & Electric.flag) : "",
        (Dark.flag & Fire.flag) : "Infernal",
        (Dark.flag & Ice.flag) : "",
        (Dark.flag & Light.flag) : "Justice",
        (Dark.flag & Plant.flag) : "Dark forest",
        (Dark.flag & Poison.flag) : "Occult",
        (Dark.flag & Water.flag) : "Petroleum",
        (Dark.flag & Wind.flag) : "Dark fog",
        (Death.flag & Earth.flag) : "Tomb",
        (Death.flag & Electric.flag) : "",
        (Death.flag & Fire.flag) : "Will-O-Wisp",
        (Death.flag & Ice.flag) : "",
        (Death.flag & Light.flag) : "Illusions",
        (Death.flag & Plant.flag) : "Hunger",
        (Death.flag & Poison.flag) : "Mortal",
        (Death.flag & Water.flag) : "Illness",
        (Death.flag & Wind.flag) : "Pollution",
        (Earth.flag & Electric.flag) : "Steel",
        (Earth.flag & Fire.flag) : "Lava",
        (Earth.flag & Ice.flag) : "",
        (Earth.flag & Light.flag) : "",
        (Earth.flag & Plant.flag) : "Nature",
        (Earth.flag & Poison.flag) : "",
        (Earth.flag & Water.flag) : "Mud",
        (Earth.flag & Wind.flag) : "Sand",
        (Electric.flag & Fire.flag) : "Induction",
        (Electric.flag & Ice.flag) : "",
        (Electric.flag & Light.flag) : "Light+",
        (Electric.flag & Plant.flag) : "Cable",
        (Electric.flag & Poison.flag) : "",
        (Electric.flag & Water.flag) : "",
        (Electric.flag & Wind.flag) : "Storm",
        (Fire.flag & Ice.flag) : "Arcane",
        (Fire.flag & Light.flag) : "Holy",
        (Fire.flag & Plant.flag) : "Ash",
        (Fire.flag & Poison.flag) : "Consume",
        (Fire.flag & Water.flag) : "Vapor",
        (Fire.flag & Wind.flag) : "Gas",
        (Ice.flag & Light.flag) : "Mirror",
        (Ice.flag & Plant.flag) : "",
        (Ice.flag & Poison.flag) : "",
        (Ice.flag & Water.flag) : "Ice+",
        (Ice.flag & Wind.flag) : "Snow",
        (Light.flag & Plant.flag) : "Growth",
        (Light.flag & Poison.flag) : "",
        (Light.flag & Water.flag) : "Bless",
        (Light.flag & Wind.flag) : "Blizzard",
        (Plant.flag & Poison.flag) : "Toxins",
        (Plant.flag & Water.flag) : "Plant+",
        (Plant.flag & Wind.flag) : "Pollen",
        (Poison.flag & Water.flag) : "",
        (Poison.flag & Wind.flag) : "Poisonous",
        (Water.flag & Wind.flag) : "Rain"
    }