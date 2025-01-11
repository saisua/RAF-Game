from .Shop import Shop

class Building(Shop):
    possible_specializations = {
        "Armors":6,
        "Weapons":5,
        "Enchantments":1
    }