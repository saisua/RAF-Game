from .Combination import Combination
from .Table import table
from .Death import Death
from .Wind import Wind


classname = "poison"
class Poison(Combination):
    name = classname
    key = table["types"][classname]

    requirements = [
        table["types"][Death.name],
        table["types"][Wind.name]
    ]

    strong = table["strong"][classname]
    weak = table["weak"][classname]
    null = table["null"][classname]
    boosted = table["boosted"][classname]
    reduced = table["reduced"][classname]

del classname