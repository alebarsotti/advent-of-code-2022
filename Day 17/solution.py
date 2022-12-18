import itertools
from collections import deque
from pprint import pprint
from time import sleep

from tqdm import tqdm

from Utils.Color import print_color, Color

ROCKS_PLACED_LIMIT = 2022

RIGHT = '>'

LEFT = '<'

MIN_Y = 1

MAX_Y = 7

MOVING_ROCK = '@'

STOPPED_ROCK = '#'

EMPTY_TILE = '.'

CHAMBER_BOTTOM = '+-------+'

ALLOWED_POSITION_VALUES = [MOVING_ROCK, EMPTY_TILE]


def get_new_empty_line():
    return [tile for tile in '|.......|']


def get_new_empty_space():
    return [get_new_empty_line(), get_new_empty_line(), get_new_empty_line()]


H_LINE = [[tile for tile in '|..@@@@.|']] + get_new_empty_space()

PLUS = [
           [tile for tile in '|...@...|'],
           [tile for tile in '|..@@@..|'],
           [tile for tile in '|...@...|'],
       ] + get_new_empty_space()

L = [
        [tile for tile in '|....@..|'],
        [tile for tile in '|....@..|'],
        [tile for tile in '|..@@@..|'],
    ] + get_new_empty_space()

V_LINE = [
             [tile for tile in '|..@....|'],
             [tile for tile in '|..@....|'],
             [tile for tile in '|..@....|'],
             [tile for tile in '|..@....|'],
         ] + get_new_empty_space()

SQUARE = [
             [tile for tile in '|..@@...|'],
             [tile for tile in '|..@@...|'],
         ] + get_new_empty_space()

rock_shapes = [H_LINE, PLUS, L, V_LINE, SQUARE]
jet_pattern = None
with open('input.txt', 'r') as file:
    for line in file:
        jet_pattern = deque([direction for direction in line.strip()])

rocks_placed = 0
chamber = [[tile for tile in CHAMBER_BOTTOM]]


def erase_empty_lines(matrix):
    first_non_empty_row = 0
    for row_index in range(len(matrix)):
        if MOVING_ROCK in matrix[row_index] or STOPPED_ROCK in matrix[row_index]:
            first_non_empty_row = row_index
            break

    return matrix[first_non_empty_row:]


def get_current_jet_direction():
    direction = jet_pattern.popleft()
    jet_pattern.append(direction)

    return direction


def positions_are_empty(matrix, new_positions):
    return all(matrix[x][y] in ALLOWED_POSITION_VALUES for x, y in new_positions)


def replace_moving_rock_positions(matrix, current_positions, new_positions, new_tile_value=MOVING_ROCK):
    for x, y in current_positions:
        matrix[x][y] = EMPTY_TILE
    for x, y in new_positions:
        matrix[x][y] = new_tile_value

    return matrix


def move_rock(matrix, current_rock_positions):
    # Get current jet direction
    jet_direction = get_current_jet_direction()
    # Move rock piece laterally if possible
    delta_y = 1 if jet_direction == '>' else -1
    new_rock_positions_lateral = [(x, y + delta_y) for x, y in current_rock_positions]
    if positions_are_empty(matrix, new_rock_positions_lateral):
        matrix = replace_moving_rock_positions(matrix, current_rock_positions, new_rock_positions_lateral)
        current_rock_positions = new_rock_positions_lateral

    # Move rock piece downwards if possible
    new_rock_positions_down = [(x + 1, y) for x, y in current_rock_positions]
    if positions_are_empty(matrix, new_rock_positions_down):
        matrix = replace_moving_rock_positions(matrix, current_rock_positions, new_rock_positions_down)
        # Continue moving rock
        return move_rock(matrix, new_rock_positions_down)
    else:
        matrix = replace_moving_rock_positions(matrix, current_rock_positions, current_rock_positions, STOPPED_ROCK)
        return matrix


def get_moving_rock_positions(rock_matrix):
    return [(index_x, index_y) for index_x, x in enumerate(rock_matrix) for index_y, y in enumerate(x) if
            y == MOVING_ROCK]


for rock in tqdm(itertools.cycle(rock_shapes)):
    if rocks_placed == ROCKS_PLACED_LIMIT:
        break
    chamber = [x.copy() for x in rock] + chamber
    moving_rock_positions = get_moving_rock_positions(rock)
    chamber = move_rock(chamber, moving_rock_positions)
    chamber = erase_empty_lines(chamber)
    rocks_placed += 1

pprint(chamber)
print(f'La torre de rocas tendrá una altura de {print_color(len(chamber) - 1, Color.CYAN)} unidades cuando la roca '
      f'número {print_color(ROCKS_PLACED_LIMIT)} finalice su movimiento.')
