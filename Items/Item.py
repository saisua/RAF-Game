from numpy import array
from .Random_item import _groups as items_dict, _all as obj_dict

DISP = 16
MASK = 2**DISP -1 

class_hash = {}
for item_class in items_dict.values():
    class_hash[item_class] = len(class_hash)+1

obj_hash = {}
for obj in obj_dict.values():
    obj_hash[obj] = len(obj_hash)+1


class Item():
    owner:"Character"
    tags:set
    important_properties:array

    def score_tags(self, tags:set) -> int:
        # Score the item based on the tags it has.
        return len(self.tags & tags)

    def __generate_base(self, level:int) -> array:
        # First the 1 is the class id, and level, each of which is half a byte.
        # Then the rest is the properties, interlaced by the "check" bytes.
        # Finally, at the end the "error" half byte, which reduce the quality of the
        # generated item, and the final "checksum" byte, which is a checksum of the
        # entire item.
        return array([0]*(1 + (len(self.important_properties)*(level+1))//2 + 1))

    def __pprint_base_schema(self, level:int) -> None:
        string = "err, check | err, err |"
        s_h = False
        for p in range(len(i_p)):
            string += f" p{p}"
            if(s_h): string += " |"
            else: string += " ,"
            s_h = not s_h
            for l in range(level):
                string += " err"
                if(s_h): string += " |"
                else: string += " ,"
                s_h = not s_h

        if(not s_h): string += " 0 |"

        string += " id, level"

        generated = self.__generate_base(level)

        print(f"Theorical: {string.count('|'+1)} | Generated: {len(generated)}")

    def __generate_checksum(self, base:array) -> int:
        base_iter = iter(base)

        checksum = 0

        # Skip the previous checksum, if there was.
        next(base_iter)
        for base_property in base_iter:
            checksum += base_property & MASK

        # Last value is the id and level.
        level = base_property & MASK

        return (checksum % level*10)

    def __check_checksum(self, base:array) -> bool:
        return self.__generate_checksum(base) == (base[0] & MASK)

    def hash(self, level:int) -> array:
        result = self.__generate_base(level)

        result[-1] = item_class[super().__class__.__name__] << DISP
        result[-1] += level

    def unhash(self, item:array) -> "Item":
        pass

    def learn(self, blueprint:array) -> None:
        pass

    def self_learn(self, base:array=None, property:int=0) -> None:
        pass


def main():
    pass

if(__name__ == "__main__"):
    main()