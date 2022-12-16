import re

from tqdm import tqdm

from Utils.Color import print_color, Color

GRID_SIZE = 4_000_000


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

    def get_tiles_adjacent_to_area(self):
        tiles = set()
        distance = self.scan_distance + 1
        for delta_x in range(distance + 1):
            tiles.add((self.x + delta_x, self.y - distance + delta_x))
            tiles.add((self.x + delta_x, self.y + distance - delta_x))
            tiles.add((self.x - delta_x, self.y - distance + delta_x))
            tiles.add((self.x - delta_x, self.y + distance - delta_x))
        return [x for x in tiles if 0 <= x[0] <= GRID_SIZE and 0 <= x[1] <= GRID_SIZE]

    def __str__(self):
        return f'Sensor({self.x},{self.y}) - Beacon({self.beacon_x},{self.beacon_y}) - ' \
               f'Manhattan Distance: {self.scan_distance}'

    def __repr__(self):
        return self.__str__()


def calculate_manhattan_distance(first_x, first_y, second_x, second_y):
    return abs(first_x - second_x) + abs(first_y - second_y)


def get_beacon_location():
    for sensor in tqdm(sensors):
        tiles_to_check = sensor.get_tiles_adjacent_to_area()
        for tile in tqdm(tiles_to_check):
            tile_is_covered = False
            for s in sensors:
                if s.covers_tile(*tile):
                    tile_is_covered = True
                    break
            if not tile_is_covered:
                return tile


sensors = []
with open('input.txt', 'r') as file:
    for line in file:
        new_sensor = Sensor(*re.findall(r'-*\d+', line.strip()))
        sensors.append(new_sensor)

beacon_location = get_beacon_location()
tuning_frequency = beacon_location[0] * GRID_SIZE + beacon_location[1]

print(f'La posición de la baliza de socorro es {print_color(beacon_location, Color.ORANGE)}.')
print(f'Su frecuencia de sintonización es {print_color(tuning_frequency, Color.ORANGE)}')
