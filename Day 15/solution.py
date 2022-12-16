import re
import sys

from tqdm import tqdm

from Utils.Color import print_color, Color

RELEVANT_Y = 2_000_000


class Sensor:
    def __init__(self, position_x, position_y, beacon_x, beacon_y):
        self.x = int(position_x)
        self.y = int(position_y)
        self.beacon_x = int(beacon_x)
        self.beacon_y = int(beacon_y)
        self.scan_distance = calculate_manhattan_distance(self.x, self.y, self.beacon_x, self.beacon_y)

    def covers_tile(self, tile_x, tile_y):
        distance_to_tile = calculate_manhattan_distance(self.x, self.y, tile_x, tile_y)
        return distance_to_tile <= self.scan_distance

    def __str__(self):
        return f'Sensor({self.x},{self.y}) - Beacon({self.beacon_x},{self.beacon_y}) - ' \
               f'Manhattan Distance: {self.scan_distance}'

    def __repr__(self):
        return self.__str__()


def calculate_manhattan_distance(first_x, first_y, second_x, second_y):
    return abs(first_x - second_x) + abs(first_y - second_y)


sensors = []
min_x = sys.maxsize
max_x = 0
with open('input.txt', 'r') as file:
    for line in file:
        sensor = Sensor(*re.findall(r'-*\d+', line.strip()))
        sensors.append(sensor)
        min_x = min(min_x, sensor.x, sensor.beacon_x)
        max_x = max(max_x, sensor.x, sensor.beacon_x)

print(f'Stats:\n\tMínimo X: {min_x}\n\tMáximo X: {max_x}')
max_scan_distance = max([sensor.scan_distance for sensor in sensors])
print(f'\tMáxima distancia de escaneo: {max_scan_distance}')
min_x -= max_scan_distance
max_x += max_scan_distance
print(f'\tNuevos extremos X:\n\t\tMínimo X: {min_x}\n\t\tMáximo X: {max_x}')

covered_tile_count = 0
for x in tqdm(range(min_x, max_x + 1)):
    tile_is_covered = False
    tile_already_occupied = False
    for sensor in sensors:
        if sensor.covers_tile(x, RELEVANT_Y):
            tile_is_covered = True
        if (x, RELEVANT_Y) in [(sensor.x, sensor.y), (sensor.beacon_x, sensor.beacon_y)]:
            tile_already_occupied = True
    covered_tile_count += 1 if tile_is_covered and not tile_already_occupied else 0

print(f'La cantidad de posiciones que no pueden contener una baliza en la fila {RELEVANT_Y} es: '
      f'{print_color(covered_tile_count, Color.ORANGE)}')
