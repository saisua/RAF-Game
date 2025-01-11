from random import randint, choice

def choose_ponderated(weights_dict:dict, other_keys:list=None,
                        remaining_points:int=1) -> tuple:
    if(other_keys is None):
        total = sum(weights_dict.values())
    else:
        total = sum(weights_dict.values()) + len(other_keys)
    
    choice = randint(1, total)
    for key, value in weights_dict.items():
        if(choice <= value):
            return key, randint(1, remaining_points)
        choice -= value

    if(other_keys is None):
        return -1, randint(1, remaining_points)

    return choice(other_keys), randint(1, remaining_points)

    