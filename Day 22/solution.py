import re
from collections import deque
from enum import Enum

from Utils.Color import print_color, Color
from Utils.Timer import timed_method

FILL_CHAR = ' '
WALL = '#'
FREE_SPACE = '.'
STARTING_ROW = 0


class Direction(Enum):
    LEFT = 0
    UP = 90
    RIGHT = 180
    DOWN = 270


direction_delta = {
    Direction.LEFT: (0, -1),
    Direction.UP: (-1, 0),
    Direction.RIGHT: (0, 1),
    Direction.DOWN: (1, 0),
}
direction_values = {
    Direction.RIGHT: 0,
    Direction.DOWN: 1,
    Direction.LEFT: 2,
    Direction.UP: 3
}


def read_notes():
    with open('input.txt', 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]
        split_index = lines.index('')
        maze = lines[0:split_index]
        instructions = lines[-1]

        return maze, instructions


def split_instructions(instructions):
    return deque(re.findall(r'\d+|\D+', instructions))


def build_maze(maze):
    maze_width = max(map(len, maze))
    maze_matrix = []
    for line in maze:
        filled_line = line.ljust(maze_width, FILL_CHAR)
        maze_matrix.append([tile for tile in filled_line])

    return maze_matrix


def move_x(current_x, new_x, new_y, maze):
    maze_height = len(maze)
    if new_x < 0 or new_x > maze_height - 1 or maze[new_x][new_y] == FILL_CHAR:
        # The movement should wrap around (end of grid or end of space reached).
        get_last = new_x < current_x
        search_range = reversed(range(maze_height)) if get_last else range(maze_height)
        # Get first/last tile in the same column that is not a fill char.
        for x in search_range:
            if maze[x][new_y] != FILL_CHAR:
                new_x = x
                break

    if maze[new_x][new_y] == FREE_SPACE:
        return new_x
    else:
        return current_x


def move_y(current_y, new_x, new_y, maze):
    maze_width = len(maze[0])
    if new_y < 0 or new_y > maze_width - 1 or maze[new_x][new_y] == FILL_CHAR:
        # The movement should wrap around (end of grid or end of space reached).
        get_last = new_y < current_y
        search_range = reversed(range(maze_width)) if get_last else range(maze_width)
        # Get first/last tile in the same row that is not a fill char.
        for y in search_range:
            if maze[new_x][y] != FILL_CHAR:
                new_y = y
                break

    if maze[new_x][new_y] == FREE_SPACE:
        return new_y
    else:
        return current_y


def perform_move(direction, steps, current_position, maze):
    current_x, current_y = current_position
    delta_x, delta_y = direction_delta[direction]
    for _ in range(steps):
        new_x = current_x + delta_x
        new_y = current_y + delta_y
        if new_x != current_x:
            current_x = move_x(current_x, new_x, new_y, maze)
        if new_y != current_y:
            current_y = move_y(current_y, new_x, new_y, maze)

    return current_x, current_y


def change_direction(direction, instruction):
    new_direction_value = (direction.value + (90 if instruction == 'R' else -90)) % 360
    return Direction(new_direction_value)


def follow_instructions(instructions, maze, starting_tile):
    current_x, current_y = starting_tile
    direction = Direction.RIGHT
    while instructions:
        instruction = instructions.popleft()
        if instruction.isdigit():
            current_x, current_y = perform_move(direction, int(instruction), (current_x, current_y), maze)
        else:
            direction = change_direction(direction, instruction)

    return current_x, current_y, direction


def adjust_partial_results(row, column, direction):
    # Rows and column indexes start from 1.
    row += 1
    column += 1
    direction_value = direction_values[direction]

    return row, column, direction_value


def solve_final_password(row, column, direction):
    return row * 1000 + column * 4 + direction


@timed_method
def main():
    maze, instructions = read_notes()

    instructions = split_instructions(instructions)

    maze = build_maze(maze)

    starting_column = maze[STARTING_ROW].index(FREE_SPACE)

    row, column, direction = follow_instructions(instructions, maze, (STARTING_ROW, starting_column))

    row, column, direction_value = adjust_partial_results(row, column, direction)

    result = solve_final_password(row, column, direction_value)

    print(f'La contraseña final es {print_color(result, Color.PURPLE)}')


if __name__ == '__main__':
    main()
