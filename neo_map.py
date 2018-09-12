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
    castle = '!'
    city = 'o'
    town = '*'
    forest = '&'
    rock = '^'

    terrain_elements = [city, town, forest, rock]
    terrain_dict = {city: cities, town: towns, forest: forests, rock: rocks, castle: castles}

    while terrain_dict[city] > 0 or terrain_dict[town] > 0 or terrain_dict[forest] > 0 or terrain_dict[rock] > 0:
        random_x = random.randrange(width)
        random_y = random.randrange(height)
        tile = terrain_elements[random.randrange(len(terrain_elements))]
        if terrain[random_x][random_y] == '.':
            terrain[random_x][random_y] = tile
            terrain_dict[tile] -= 1

    while castle_not_placed and castles != 0:
        random_x = random.randrange(width)
        random_y = random.randrange(height)
        if terrain[random_x][random_y] == '.':
            terrain[random_x][random_y] = castle
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
board_area = board_x * board_y
cities = 3
towns = 3
forests = 10
rocks = 5
castles = 3
total_elements = cities + towns + forests + rocks + castles + 1

if total_elements < board_area:
    terrain = initialize_terrain(board_x, board_y)
    board = generate_board(terrain, cities, towns, forests, rocks, castles)
    print_map(board)
else:
    print("Map is too small for the number of elements")

