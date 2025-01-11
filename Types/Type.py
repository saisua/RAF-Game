from typing import Set

class Type:
    name:str
    flag:int = 0    
    actual_flag:int = 1
    flag_dict:dict = {}

    strong:Set[int]
    weak:Set[int]
    null:Set[int]
    boosted:Set[int]
    reduced:Set[int]

    def __init__(self):
        if(self.__class__.flag == 0):
            self.__class__.flag = 2 << self.actual_flag
            
            self.flag_dict[self.__class__] = self.flag

            Type.actual_flag += 1
