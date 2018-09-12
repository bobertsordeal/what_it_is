import random

def generateMap(board_size):
    map_elements = ['c','t','f','_','r','_']
    map_dict = {'c':2,'t':4,'f':4,'_':25,'r':2}

    my_map = []
    for i in range(board_size):
        my_map.append([])
        for j in range(board_size):
            placed = False
            while(not placed):
                tile = map_elements[random.randrange(board_size+1)]    
                if map_dict[tile]:
                    map_dict[tile] -= 1
                    placed = True
                
            
            my_map[i].append(tile)
        
    my_map[random.randrange(board_size)][ random.randrange(board_size)] = "x"
    
    return my_map

def printMap(my_map):
    for i in range(len(my_map)):
        for j in range(len(my_map)):
            print(my_map[i][j], end=" ")
        print("")
        
my_map = generateMap(5)
printMap(my_map)
