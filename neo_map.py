import random


def initialize_terrain(width, height):
    board = []
    line = []

    for x in range(width):
        for y in range(height):
            line.append('.')

        board.append(line)
        line = []

    return board


def generate_board(terrain, cities, towns, forests, rocks, castles):
    width = len(terrain)
    height = len(terrain[0])
    castle_not_placed = True
    terrain_elements = ['c', 't', 'f', 'r']
    terrain_dict = {'c': cities, 't': towns, 'f': forests, 'r': rocks}

    while terrain_dict['c'] > 0 or terrain_dict['t'] > 0 or terrain_dict['f'] > 0 or terrain_dict['r'] > 0:
        random_x = random.randrange(width)
        random_y = random.randrange(height)
        tile = terrain_elements[random.randrange(len(terrain_elements))]
        terrain[random_x][random_y] = tile
        terrain_dict[tile] -= 1

    while castle_not_placed and castles != 0:
        random_x = random.randrange(width)
        random_y = random.randrange(height)
        if terrain[random_x][random_y] == '.':
            terrain[random_x][random_y] = 'X'
            castles -= 1

        if castles == 0:
            castle_not_placed = False

    return terrain


def print_map(game_map):
    build_map = ""
    for row in game_map:
        for column in row:
            build_map += column + "   "
        build_map += '\n'
        build_map += '\n'
    print(build_map)


board_x = 10
board_y = 10
cities = 3
towns = 3
forests = 10
rocks = 5
castles = 1

terrain = initialize_terrain(10, 10)
board = generate_board(terrain, cities, towns, forests, rocks, castles)
print_map(board)
