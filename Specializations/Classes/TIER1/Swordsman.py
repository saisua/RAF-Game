"""
    Swordsman start to learn how to fight
    and to use some basic weapons.
"""

from .Tier1 import T1_REQUIREMENTS
from ..Class import Class
from Items.Tags import *

class Rogue(Class):
    requirements = Class.requirements | T1_REQUIREMENTS

    preferences:dict = {
        "Items":{
            "Abilities":{},
            "Armors":{},
            "Pets":{},
            "Spells":{},
            "Weapons":{MELEE:1}
        },
        "Attributes":{
            "evasion":2,
            "precission":1,
            "strength":1,
            "speed":2,
            "attack_speed":2,
            "knock":0,
            "stun":0,
            "weapon_rate":0,
            "weapon_strength":0,
            "magic":0,
            "magic_strength":0,
            "defense":0,
            "pet_rate":0,
            "life":0,
            "magic_defense":0,
            "ability_rate":1
        }
    }