"""
    Apprendices learn the basics of magic,
    and start casting basic spells
"""

from .Tier1 import T1_REQUIREMENTS
from ..Class import Class
from Items.Tags import *

class Apprendice(Class):
    requirements = Class.requirements | T1_REQUIREMENTS

    preferences:dict = {
        "Items":{
            "Abilities":{},
            "Armors":{},
            "Pets":{},
            "Spells":{OFFENSIVE:1},
            "Weapons":{MAGICAL:1}
        },
        "Attributes":{
            "evasion":1,
            "precission":0,
            "strength":0,
            "speed":1,
            "attack_speed":1,
            "knock":1,
            "stun":0,
            "weapon_rate":0,
            "weapon_strength":0,
            "magic":3,
            "magic_strength":3,
            "defense":0,
            "pet_rate":0,
            "life":1,
            "magic_defense":1,
            "ability_rate":1
        }
    }