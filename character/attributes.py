from dataclasses import dataclass
from random import randint

# Evasion
# Precission
# Strength
# Speed
# AttackSpeed
# Knock
# Stun
# Weapon_rate
# Weapon_strength
# Magic
# Magic_strength
# Defense
# Pet_rate

class Attr_creation():
    names = [
        "evasion",
        "precission",
        "strength",
        "speed",
        "attack_speed",
        "knock",
        "stun",
        "weapon_rate",
        "weapon_strength",
        "magic",
        "magic_strength",
        "defense",
        "pet_rate",
        "life",
        "magic_defense",
        "ability_rate"
    ]

    level_up = {
        "strength":45,
        "speed":20,
        "attack_speed":20,
        "weapon_strength":50,
        "magic":60,
        "magic_strength":50,
        "defense":40,
        "life":100,
        "magic_defense":40,
    }

    data = {
        # Percentage over 100
        "EVASSION_MIN" : 0,
        "EVASSION_MAX" : 20,

        # Percentage over 100
        "PRECISSION_MIN" : 80,
        "PRECISSION_MAX" : 100,

        "STRENGTH_MIN" : 30,
        "STRENGTH_MAX" : 40,

        "SPEED_MIN" : 10,
        "SPEED_MAX" : 30,

        "ATTACKSPEED_MIN" : 20,
        "ATTACKSPEED_MAX" : 30,

        # Percentage over 100 per turn (with conditions)
        "KNOCK_MIN" : 0,
        "KNOCK_MAX" : 25,

        # Percentage over 100 per turn (with conditions)
        "STUN_MIN" : 0,
        "STUN_MAX" : 3,

        # Percentage over 100 per turn
        "WEAPONRATE_MIN" : 10,
        "WEAPONRATE_MAX" : 30,

        "WEAPONSTRENGTH_MIN" : 10,
        "WEAPONSTRENGTH_MAX" : 35,

        "MAGIC_MIN" : 10,
        "MAGIC_MAX" : 120,

        "MAGICSTRENGTH_MIN" : 20,
        "MAGICSTRENGTH_MAX" : 40,

        "DEFENSE_MIN" : 25,
        "DEFENSE_MAX" : 35,

        #Percentage over 100 per turn
        "PET_MIN" : 0,
        "PET_MAX" : 25,

        "LIFE_MIN" : 100,
        "LIFE_MAX" : 200,

        "MAGICDEFENSE_MIN" : 15,
        "MAGICDEFENSE_MAX" : 35,

        #Percentage over 100 per turn
        "ABILITYRATE_MIN" : 15,
        "ABILITYRATE_MAX" : 25
    }

    descriptions = {
        # Evassion
        0:{
            # Precission
            1:"Ninja",
            # Strength
            2:"Sniper",
            # Speed
            3:"Sneaky",
            # Attack speed
            4:"Sneaky",
            # Knock
            5:"Annoying",
            # Stun
            6:"Annoying",
            # Weapon rate
            7:"Gadgetman",
            # Weapon strength
            8:"Rogue",
            # Magic
            9:"Ocultist",
            # Magic strength
            10:"Ocultist",
            # Defense
            11:"Unhitable",
            # Pet rate
            12:"Unreachable",
            # Life
            13:"Survivor",
            # Magic defense
            14:"Unhitable",
            # Ability rate
            15:"Support"
        },
        # Precission
        1:{
            # Strength
            2:"Sniper",
            # Speed
            3:"Opportunist",
            # Attack speed
            4:"Martial artist",
            # Knock
            5:"Martial artist",
            # Stun
            6:"Martial artist",
            # Weapon rate
            7:"Skilled weaponist",
            # Weapon strength
            8:"Rogue",
            # Magic
            9:"Ocultist",
            # Magic strength
            10:"Mage",
            # Defense
            11:"Safe player",
            # Pet rate
            12:"Trainer",
            # Life
            13:"Safe player",
            # Magic defense
            14:"Safe player",
            # Ability rate
            15:"Skilled sniper"
        },
        # Strength
        2:{
            # Speed
            3:"Warrior",
            # Attack speed
            4:"Hard hitting",
            # Knock
            5:"Martial artist",
            # Stun
            6:"Martial artist",
            # Weapon rate
            7:"Weaponist",
            # Weapon strength
            8:"Melee weaponist",
            # Magic
            9:"Phisical mage",
            # Magic strength
            10:"Strength itself",
            # Defense
            11:"Tank",
            # Pet rate
            12:"Trainer",
            # Life
            13:"Warrior",
            # Magic defense
            14:"Tank",
            # Ability rate
            15:"Tower"
        },
        # Speed
        3:{
            # Attack speed
            4:"Ninja",
            # Knock
            5:"Ninja",
            # Stun
            6:"Ninja",
            # Weapon rate
            7:"Safe weaponist",
            # Weapon strength
            8:"Rogue",
            # Magic
            9:"Safe mage",
            # Magic strength
            10:"Safe mage",
            # Defense
            11:"Unhitable",
            # Pet rate
            12:"Unreachable",
            # Life
            13:"Survivor",
            # Magic defense
            14:"Safe mage",
            # Ability rate
            15:"Rogue"
        },
        # Attack speed
        4:{
            # Knock
            5:"Crowd controller",
            # Stun
            6:"Crowd controller",
            # Weapon rate
            7:"Weaponist",
            # Weapon strength
            8:"Weaponist",
            # Magic
            9:"Spammer",
            # Magic strength
            10:"Hard hitting",
            # Defense
            11:"Consistent",
            # Pet rate
            12:"Beasts friend",
            # Life
            13:"Hard to deal-with",
            # Magic defense
            14:"Hard to deal-with",
            # Ability rate
            15:"Spammer"
        },
        # Knock
        5:{
            # Stun
            6:"Crowd controller",
            # Weapon rate
            7:"Weaponist",
            # Weapon strength
            8:"Spike barrier",
            # Magic
            9:"Magic barrier",
            # Magic strength
            10:"Spike barrier",
            # Defense
            11:"Barrier",
            # Pet rate
            12:"Hog",
            # Life
            13:"Body builder",
            # Magic defense
            14:"Magician",
            # Ability rate
            15:"Rogue"
        },
        # Stun
        6:{
            # Weapon rate
            7:"Weaponist",
            # Weapon strength
            8:"Big hammer",
            # Magic
            9:"Crowd controller",
            # Magic strength
            10:"Magician",
            # Defense
            11:"Crowd Controller",
            # Pet rate
            12:"Hog",
            # Life
            13:"Body builder",
            # Magic defense
            14:"Magician",
            # Ability rate
            15:"Rogue"
        },
        # Weapon rate
        7:{
            # Weapon strength
            8:"Weaponist",
            # Magic
            9:"Enchancer",
            # Magic strength
            10:"Gadgetman",
            # Defense
            11:"Gadgetman",
            # Pet rate
            12:"Claw",
            # Life
            13:"Warrior",
            # Magic defense
            14:"Gadgetman",
            # Ability rate
            15:"Support"
        },
        # Weapon strength
        8:{
            # Magic
            9:"Enchancer",
            # Magic strength
            10:"Hard hitting",
            # Defense
            11:"Barrier",
            # Pet rate
            12:"Fang",
            # Life
            13:"Hard hitting",
            # Magic defense
            14:"Enchancer",
            # Ability rate
            15:"Hard hitting"
        },
        # Magic
        9:{
            # Magic strength
            10:"Mage",
            # Defense
            11:"Magic barrier",
            # Pet rate
            12:"Elementarist",
            # Life
            13:"Magic barrier",
            # Magic defense
            14:"Safe mage",
            # Ability rate
            15:"Trickster"
        },
        # Magic strength
        10:{
            # Defense
            11:"Magic barrier",
            # Pet rate
            12:"Elementarist",
            # Life
            13:"Magic barrier",
            # Magic defense
            14:"Mage",
            # Ability rate
            15:"Mage"
        },
        # Defense
        11:{
            # Pet rate
            12:"Safe player",
            # Life
            13:"Tank",
            # Magic defense
            14:"Special tank",
            # Ability rate
            15:"Tank    "
        },
        # Pet rate
        12:{
            # Life
            13:"Survivor",
            # Magic defense
            14:"Survivor",
            # Ability rate
            15:"Damage"
        },
        # Life
        13:{
            # Magic defense
            14:"Magic barrier",
            # Ability rate
            15:"Support"
        },
        # Magic defense
        14:{
            # Ability rate
            15:"Tank"
        }
        # Ability rate
    }

    PERCENTAGE_ITEM = 20 # 1/value

    total = sum([(-1**(num%2+2))*val for num, val in enumerate(data.values())])
    length = len(names)

    @staticmethod
    def get() -> list:
        return Attr_creation.data.values()

    @staticmethod
    def create(points:int=total) -> "Attributes":
        data_iter = iter(Attr_creation.data.values())
        data_num = 0

        result = []
        attr_min = next(data_iter, None)

        max_1 = 0
        max_1_value = 0
        max_2 = 0
        max_2_value = 0

        profile_value = 0

        while(not attr_min is None and points != 0):
            attr = next(data_iter)

            attr_value = randint(attr_min, attr)
            if(attr_value < points):
                attr_value = points

            result.append(attr_value)

            points -= attr_value

            attr_value = (attr_value - attr_min) / (attr - attr_min)

            if(attr_value > max_1_value):
                max_2, max_1 = max_1, data_num
                max_2_value, max_1_value = max_1_value, attr_value
            elif(attr_value > max_2_value):
                max_2 = data_num
                max_2_value = attr_value

            profile_value += attr_value

            attr_min = next(data_iter, None)
            data_num += 1 

        des_dict = {max_1:max_1_value, max_2:max_2_value}
        descript = sorted([max_1,max_2])

        result_dict = dict(zip(Attr_creation.names, result))
        result_dict["description"] = f"the {Attr_creation.descriptions[descript[0]][descript[1]]}"
        result_dict["profile_value"] = profile_value/Attr_creation.length

        return (Attributes(**result_dict),[Attr_creation.names[desc] for desc in descript 
                                            if not randint(0, Attr_creation.PERCENTAGE_ITEM)])

@dataclass
class Attributes():
    weapon_strength:int
    weapon_rate:int
    stun:int
    strength:int
    speed:int
    profile_value:float
    precission:int
    pet_rate:int
    magic_strength:int
    magic_defense:int
    magic:int
    life:int
    knock:int
    evasion:int
    description:str
    defense:int
    attack_speed:int
    ability_rate:int

    _aliases = {"Pet":"pet_rate", "Weapon":"weapon_rate", "Ability":"ability_rate"}

    def __iter__(self):
        result = []
        for attr_name in dir(self)[::-1]:
            if(attr_name.startswith('_')): break

            result.append((attr_name, self.__getattribute__(attr_name)))

        return iter(result)

    def _get(self, name:str, default=None):
        try:
            return self.__getattribute__(self._aliases.get(name, name))
        except:
            return default

    def _set(self, name:str, value, operation:callable=lambda bef, aft: aft):
        exec(f"self.{self._aliases.get(name, name)} = {operation(self._get(name), value)}")