import string

from simpleai.search import SearchProblem, uniform_cost

from Utils.Color import print_color, Color

GOAL = 'E'
START = ['S', 'a']

height_values = ['S'] + list(string.ascii_lowercase) + [GOAL]


def get_surrounding_positions(state):
    x, y = state
    # List adjacent positions
    surrounding_positions = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
    # Discard positions outside grid bounds
    return list(filter(lambda pos: 0 <= pos[0] < map_height and 0 <= pos[1] < map_width, surrounding_positions))


def is_valid_next_position(position_height, next_position):
    next_position_height = get_position_height(next_position)
    pos_height_value = height_values.index(position_height)
    next_pos_height_value = height_values.index(next_position_height)

    # Movement is only possible when the next position has lower or equal height, or is only 1 above.
    return pos_height_value + 1 >= next_pos_height_value


def get_position_height(position):
    x, y = position
    return heightmap[x][y]


class ClimbingProblem(SearchProblem):
    def actions(self, state):
        position_height = get_position_height(state)
        if position_height == GOAL:
            return []

        surrounding_positions = get_surrounding_positions(state)
        return list(filter(lambda pos: is_valid_next_position(position_height, pos), surrounding_positions))

    def result(self, state, action):
        return action

    def cost(self, state, action, state2):
        return 1

    def is_goal(self, state):
        return get_position_height(state) == GOAL


heightmap = []
with open('input.txt', 'r') as file:
    for line in file:
        heightmap.append([height for height in line.strip()])

map_width = len(heightmap[0])
map_height = len(heightmap)


def get_starting_positions():
    positions = []
    for row_index, row in enumerate(heightmap):
        for column_index, position in enumerate(row):
            if position in START:
                positions.append((row_index, column_index))
    return positions


starting_positions = get_starting_positions()

results = []
for start in starting_positions:
    climbing_problem = ClimbingProblem(initial_state=start)
    search_result = uniform_cost(climbing_problem, graph_search=True)
    # Avoid counting the initial state.
    if search_result is not None:
        steps_taken = len(search_result.path()) - 1
        results.append(steps_taken)

number_of_steps = min(results)

print(f'La cantidad mínima de pasos necesarios para desplazarse desde cualquier posición de altura mínima '
      f'hasta el punto con mejor señal es {print_color(number_of_steps, Color.CYAN)}')
