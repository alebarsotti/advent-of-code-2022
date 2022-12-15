import itertools
import os
import sys
from collections import namedtuple
from enum import Enum

from Utils.Color import print_color, Color

POSITION_SEPARATOR = ' -> '
COORDINATES_SEPARATOR = ','
ROCK = '#'
AIR = '.'
SAND = 'o'
SAND_STARTING_POSITION = (0, 500)

Directions = namedtuple('Color', ['delta_y'])


class Direction(Enum):

    @property
    def delta_y(self):
        return self.value.delta_y

    LEFT = Directions(-1)
    RIGHT = Directions(1)
    DOWN = Directions(0)


path_sections_list = []
max_x = 0
max_y = 0
min_y = sys.maxsize


def put_rocks():
    for path_start, path_end in path_sections_list:
        start_x, start_y = path_start
        end_x, end_y = path_end
        if start_x != end_x:
            for cave_x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                cave[cave_x][start_y] = ROCK
        else:
            for cave_y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                cave[start_x][cave_y] = ROCK


def move_to_bottom(sand_position):
    sand_x, sand_y = sand_position
    for row_index in range(sand_x, len(cave)):
        if cave[row_index][sand_y] != AIR:
            return row_index - 1, sand_y
    return sand_position


def move_to_side(sand_position, direction):
    sand_x, sand_y = sand_position
    new_x = sand_x + 1
    new_y = sand_y + direction.delta_y
    if 0 <= new_y <= len(cave[0]) and new_x <= len(cave) and cave[new_x][new_y] == AIR:
        return new_x, new_y
    return sand_position


def move_sand(sand_position):
    initial_position = sand_position
    new_position = move_to_bottom(initial_position)
    if initial_position != new_position:
        return new_position
    new_position = move_to_side(new_position, Direction.LEFT)
    if initial_position != new_position:
        return new_position
    return move_to_side(new_position, Direction.RIGHT)


def clear_output():
    if os.name == 'posix':
        os.system('clear')
    # screen clear for windows
    else:
        os.system('cls')


def print_cave():
    clear_output()
    for row in cave:
        for y_index, tile in enumerate(row):
            if y_index >= min_y:
                print_tile(tile)
        print()
    print()


def print_tile(tile):
    color = ''
    if tile == AIR:
        tile = ' '
    elif tile == ROCK:
        color = Color.LIGHT_GRAY
    elif tile == SAND:
        color = Color.YELLOW
    text = print_color(tile, color)
    print(text, end='')


with open('input.txt', 'r') as file:
    for line in file:
        path_positions = line.strip().split(POSITION_SEPARATOR)
        for index, position in enumerate(path_positions):
            y, x = position.split(COORDINATES_SEPARATOR)
            x = int(x)
            y = int(y)
            path_positions[index] = (x, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)
        path_sections_list.extend([x for x in itertools.pairwise(path_positions)])

cave = [[AIR for x in range(max_y + 1)] for y in range(max_x + 1)]

put_rocks()

sand_resting_count = 0
try:
    while True:
        new_sand_position = SAND_STARTING_POSITION

        while True:
            initial_sand_position = new_sand_position
            new_sand_position = move_sand(initial_sand_position)
            if new_sand_position == initial_sand_position:
                cave[new_sand_position[0]][new_sand_position[1]] = SAND
                sand_resting_count += 1
                break
except IndexError:
    print_cave()

print(f'La cantidad de unidades de arena que se ubican en descanso sobre las rocas '
      f'es: {print_color(sand_resting_count, Color.ORANGE)}')
