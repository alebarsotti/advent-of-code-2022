import time
from collections import deque

from Utils.Color import print_color, Color

START_VALUE = 0


class ListItem:
    def __init__(self, value):
        self.value = int(value)

    def __str__(self):
        return f'Value: {self.value}'

    def __repr__(self):
        return self.__str__()


def read_original_list():
    with open('input.txt', 'r') as file:
        return deque([ListItem(value) for value in file.readlines()])


def apply_mixing(original_list: deque):
    list_size = len(original_list)
    rearranged_list = deque(original_list)

    while original_list:
        element = original_list.popleft()
        value = element.value
        current_index = rearranged_list.index(element)
        # Rotate until current element is at the start.
        rearranged_list.rotate(-current_index)
        # Remove element from list.
        element = rearranged_list.popleft()
        # Rotate list by element value (swap sign is necessary since rotate behaves opposite as intended).
        rearranged_list.rotate(-value)
        # Put element again at the start, in its new position.
        rearranged_list.appendleft(element)

    return rearranged_list


def get_grove_coordinates(mixing_result):
    list_size = len(mixing_result)
    start_index = next((i for i, element in enumerate(mixing_result) if element.value == START_VALUE), None)
    coordinates = []
    for coord_position in (1000, 2000, 3000):
        coord_index = (start_index + coord_position) % list_size
        coordinates.append(mixing_result[coord_index].value)

    return coordinates


if __name__ == '__main__':
    start = time.perf_counter()
    original_list = read_original_list()

    mixing_result = apply_mixing(original_list)

    coord_x, coord_y, coord_z = get_grove_coordinates(mixing_result)

    end = time.perf_counter()
    print(f'Tiempo de procesamiento: {end - start:.6f} segundos')
    print(f'Las coordenadas de la arboleda son ({print_color(coord_x, Color.GREEN)}, '
          f'{print_color(coord_y, Color.GREEN)}, {print_color(coord_z, Color.GREEN)}).')
    print(f'La suma de las coordenadas es {print_color(coord_x + coord_y + coord_z, Color.GREEN)}.')
