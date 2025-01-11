from .Death import Death
from .Fire import Fire
from .Light import Light
from .Nature import Nature
from .Water import Water
from .Wind import Wind
from .Rock import Rock
from .Poison import Poison

table = {
    "types":{
        Death.name : Death,
        Fire.name : Fire,
        Light.name : Light,
        Nature.name : Nature,
        Poison.name : Poison,
        Rock.name : Rock,
        Water.name : Water,
        Wind.name : Wind,
    }
}

typ = tuple(table.keys())
typ = dict((key, typ.index(key)) for key in typ)

table.update({
    "strong":{
        Death.name : {
            typ[Wind.name],
        },
        Fire.name : {
            typ[Nature.name],
            typ[Wind.name]
        },
        Light.name : {
            typ[Death.name],
            typ[Poison.name]
        },
        Nature.name : {
            typ[Water.name],
            typ[Light.name]
        },
        Poison.name : {
            typ[Nature.name],
        },
        Rock.name : {
            typ[Light.name],
            typ[Nature.name]
        },
        Water.name : {
            typ[Fire.name],
            typ[Rock.name]
        },
        Wind.name : {
            typ[Rock.name]
        },
    },
    "weak":{
        Death.name : {},
        Fire.name : {},
        Light.name : {},
        Nature.name : {},
        Poison.name : {},
        Rock.name : {},
        Water.name : {},
        Wind.name : {},
    },
    "null":{
        Death.name : {},
        Fire.name : {},
        Light.name : {},
        Nature.name : {},
        Poison.name : {},
        Rock.name : {},
        Water.name : {},
        Wind.name : {},
    },
    # A weird property. If something has a type as a passive
    # attribute, and gets hit by some type from this list, 
    # it gets an increased damage received
    "boosted":{
        Death.name : {},
        Fire.name : {},
        Light.name : {},
        Nature.name : {},
        Poison.name : {},
        Rock.name : {},
        Water.name : {},
        Wind.name : {},
    },
    "reduced":{
        Death.name : {},
        Fire.name : {},
        Light.name : {},
        Nature.name : {},
        Poison.name : {},
        Rock.name : {},
        Water.name : {},
        Wind.name : {},
    }
})

del typ