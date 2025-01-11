import numpy
import json
from typing import Tuple, List, Iterable
from random import shuffle, random

# pos[(len(pos)//2+n)%len(pos)] must be inverse mov of pos[n]
# As so, pos must be even
# I keep the string for debugging purposes
pos:dict = {
    "UP" : (0,(0,-1), "right"),
    "RIGHT" : (1,(1,0), "up"),
    "DOWN" : (2,(0,1), "left"),
    "LEFT" : (3,(-1,0), "down")
}
# Reverse dictionary by vector-string
rev_pos:dict = {
    "0,-1" : (0,(0,-1), "right"),
    "1,0" : (1,(1,0), "up"),
    "0,1" : (2,(0,1), "left"),
    "-1,0" : (3,(-1,0), "down")
}

def main() -> None:
    maze = maze_creator()

    print(printify(maze))

    #if('y' in input("guardar?")):
    #    with open("laberinto_.json", 'w') as file:
    #        file.write(json.dumps(maze))

def printify(maze:numpy.array) -> str:
    """
        Returns the representation of the maze walls
        based on the binary representation of the number given

        Parameters
        ----------
        num : int
            The integer used to get the representation of the maze

        Returns
        -------
        str
            A custom string set to be visually appealing when mapped
            into the maze
    """
    positions = tuple(pos.keys())
    # mask
    m = dict((pos_name, 2**positions.index(pos_name)) for pos_name in positions)

    pretty = {0:'O',
            m["UP"]:'U',
            m["RIGHT"]:'[',
            m["UP"]+m["RIGHT"]:'╚',
            m["DOWN"]:'^',
            m["UP"]+m["DOWN"]:'║', 
            m["RIGHT"]+m["DOWN"]:'╔', 
            m["UP"]+m["RIGHT"]+m["DOWN"]:'╠',
            m["LEFT"]:']',
            m["UP"]+m["LEFT"]:'╝', 
            m["RIGHT"]+m["LEFT"]:'=', 
            m["UP"]+m["RIGHT"]+m["LEFT"]:'╩', 
            m["DOWN"]+m["LEFT"]:'╗', 
            m["UP"]+m["DOWN"]+m["LEFT"]:'╣', 
            m["RIGHT"]+m["DOWN"]+m["LEFT"]:'╦', 
            m["UP"]+m["RIGHT"]+m["DOWN"]+m["LEFT"]:'╬'}

    result = ['']

    for y in maze:
        for cell in y:
            result.append(pretty[cell])
        result.append('\n')

    return ' '.join(result[:-1])




def pluspos(start:Tuple[int, int], move:Tuple[int, Tuple[int, int]]) -> Tuple[int, int]:
    """
        Specialized 2D vector sum

        Parameters
        ----------
        start : Tuple[int, int]
            A vector of two integers to be sumed to move[1]

        move : Tuple[int, Tuple[int, int]]
            Parameter set to match the data structure built in maze_creator(),
            where only the second element is used. This element must match
            the description of the argument start

        Returns
        -------
        Tuple[int, int]
            A vector of two integers result of the sum of start and move[1]
    """
    return (start[0]+move[1][0],start[1]+move[1][1])

# This version shoud be able to operate with vectors of any size *UNUSED*
def pluspos_scale(*args:Iterable[Iterable[int]], op:"operator"=sum) -> Tuple[int]:
    """
        Generic vector operator function

        Parameters
        ----------
        *args : Iterable[Iterable[int]]
            Any number of iterables, where all the iterables have the same length

        op : operator
            Any operator which takes a vector as the only parameter

        Returns
        -------
        Tuple[int]
            A tuple for the operation of the operator for every element of the vectors,
            the size of which will match all individual vectors given as parameter
    """
    return tuple(op((vector[dim] for vector in args)) for dim in range(len(args[0])))



def maze_creator(size:Tuple[int,int]=(35,84), *,
                start:Tuple[int,int]=(0,0), end:Tuple[int,int]=None,
                diverge:bool=True, diverge_end_chance:float=0,
                remove_non_connected:bool=True) -> numpy.array:
    """
        Returns a maze created with a path between start and end

        Parameters
        ----------
        size : Tuple[int,int]
            The size of final maze. Each int represents a dimension (x,y)

        start : Tuple[int,int]
            The point where the algorithm will start to create the path

        end : Tuple[int,int]
            The point where the algorithm will end the path

        diverge : bool
            If the algorithm should create fake paths to fill the maze

        Returns
        -------
        numpy.array
            An int array where each number is a point of the maze,
            and its binary representation contains wall placement information
    """
    mapa = numpy.zeros(size, dtype=int)
    explored = numpy.zeros(size, dtype=bool)

    # If no custom end is selected, it is set to the last point
    if(end is None): end = tuple([dim-1 for dim in size])

    explored[start] = True
    position = tuple(start)

    movements = list(pos.values())
    path = [start]
    connected = set((end,))

    def check(start:Tuple[int]) -> bool:
        return all([-1 < dim < size[num] for num, dim in enumerate(start)])

    def is_valid(pos:List[int], mov:Tuple[int, Tuple[int, int]], state:numpy.array) -> bool:
        start = pluspos(pos,mov)
        #print(f"Check {start}")
        if(not check(start) or state[start]):
            #print("OoBounds")
            return False

        return True
    ####

    last = None

    # Create a path from start to end using DFS
    while(position != end):
        #print(position, end='\r')
        shuffle(movements)

        for next_mov in movements:
            if(is_valid(position, next_mov, explored)):
                break
        else:
            explored[position] = True
            mapa[position] = 0
            position = path.pop()
            last = None
            continue

        #print()

        walls = ['0' for _ in range(len(movements))]

        if(not last is None):
            walls[(last+(len(movements)//2))%len(movements)] = '1'
        elif(len(path) > 1):
            last = rev_pos[','.join(map(str, ((position[0]-path[-1][0]),(position[1]-path[-1][1]))))][0]

            walls[(last+(len(movements)//2))%len(movements)] = '1'

        walls[next_mov[0]] = '1'

        last = next_mov[0]

        mapa[position] = int(''.join(walls),2)
        path.append(position)
        explored[position] = True

        position = pluspos(position, next_mov)
    ####

    connected.update(path)

    del explored

    walls = ['0','0','0','0']
    walls[(last+(len(movements)//2))%len(movements)] = '1'

    mapa[position] = int(''.join(walls),2)
    #print(position)

    #for y in mapa:
    #    print(' '.join(map(printify, y)))

    if(diverge):
        # For every empty point, start a new path until
        # you hit an already existing path
        for posy, y in enumerate(mapa):
            for posx, x in enumerate(y):
                if(not x):
                    path.clear()
                    
                    position = (posy,posx)
                    last = None
                    path.append(position)

                    while(True):
                        shuffle(movements)

                        for next_mov in movements:
                            if(last and next_mov[0] == (last+(len(movements)//2))%len(movements)):
                                continue
                            next_pos = pluspos(position, next_mov)
                            if(check(next_pos)):
                                break
                        
                        # Add the chosen movement to the path taken
                        path.append(position)
                        if(mapa[next_pos]):
                            # If the position is connected to the
                            # main way, it has to be added as connected
                            if(next_pos in connected):
                                connected.update(path)
                                
                            walls = ['0' for _ in range(len(movements))]

                            if(not last is None):
                                walls[(last+(len(movements)//2))%len(movements)] = '1'
                            walls[next_mov[0]] = '1'

                            last = next_mov[0]

                            #explored[position] = True
                            mapa[position] = int(''.join(walls), 2)

                            direction = ['0','0','0','0']
                            direction[(next_mov[0]+(len(movements)//2))%len(movements)] = '1'
                            #print(position, end=' -> ')
                            position = next_pos
                            #print(position)

                            #print(f"{mapa[position]} | {direction} => ", end='')

                            mapa[position] = mapa[position] | int(''.join(direction), 2)
                            #print(mapa[position])
                            break
                        ####

                        walls = ['0' for _ in range(len(movements))]

                        if(not last is None):
                            walls[(last+(len(movements)//2))%len(movements)] = '1'
                        walls[next_mov[0]] = '1'

                        last = next_mov[0]

                        #explored[position] = True
                        mapa[position] = int(''.join(walls), 2)
                        position = next_pos

                        if(random() <= diverge_end_chance):
                            break
    ####################

    # If we have to remove all non connected paths, simply
    # check all map one by one, setting all non-connected to zero
    if(remove_non_connected):
        for y, sub in enumerate(mapa):
            for x in range(len(sub)):
                position = (y,x)
                if(position not in connected):
                    mapa[position] = 0



    return mapa

if __name__ == "__main__":
    main()