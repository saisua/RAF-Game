from Specializations.Specialization import Specialization
from ../Specialization import Specialization

class Class(Specialization):
    # tags
    preferences:dict = {
        "Items":{
            "Abilities":{},
            "Armors":{},
            "Pets":{},
            "Spells":{},
            "Weapons":{}
        },
        "Attributes":{
            "evasion":0,
            "precission":0,
            "strength":0,
            "speed":0,
            "attack_speed":0,
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
            "ability_rate":0
        }
    }
    
    requirements = {
        "class":lambda classes, max_classes=1: len(classes) < max_classes
    }