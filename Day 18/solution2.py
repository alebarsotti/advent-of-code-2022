import time
from collections import deque

from Utils.Color import print_color, Color

CUBE_SIDES = 6

water_cubes = set()
exterior_cubes = set()


def calculate_cube_visible_sides(x, y, z):
    count = 0
    count += (x + 1, y, z) in water_cubes
    count += (x - 1, y, z) in water_cubes
    count += (x, y + 1, z) in water_cubes
    count += (x, y - 1, z) in water_cubes
    count += (x, y, z + 1) in water_cubes
    count += (x, y, z - 1) in water_cubes

    return count


def get_cube_ranges(x, y, z):
    return range(0, x + 2), range(0, y + 2), range(0, z + 2)


def count_total_visible_sides(points_to_consider=None):
    visible_sides = 0
    for x, y_dict in droplet_map.items():
        for y, z_set in y_dict.items():
            for z in z_set:
                if points_to_consider and (x, y, z) not in points_to_consider:
                    continue
                visible_sides += calculate_cube_visible_sides(x, y, z)
    return visible_sides


def get_adjacent_cubes(init_point, range_x, range_y, range_z):
    x, y, z = init_point
    adjacent_points = [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]

    return [(x, y, z) for x, y, z in adjacent_points if x in range_x and y in range_y and z in range_z]


def droplet_contains_cube(x, y, z):
    return z in droplet_map.get(x, {}).get(y, ())


def find_exterior_cubes(range_x, range_y, range_z, init_point=(0, 0, 0)):
    cube_queue = deque()
    cube_queue.append(init_point)
    while cube_queue:
        cube = cube_queue.popleft()
        # Mark cube as water.
        water_cubes.add(cube)
        # Check adjacent cubes.
        adjacent_cubes = get_adjacent_cubes(cube, range_x, range_y, range_z)
        for x, y, z in adjacent_cubes:
            if droplet_contains_cube(x, y, z):
                # Mark cube as exterior.
                exterior_cubes.add((x, y, z))
            elif (x, y, z) not in water_cubes and (x, y, z) not in cube_queue:
                # Add remaining cubes to queue if not already visited.
                cube_queue.append((x, y, z))
                # find_exterior_cubes(range_x, range_y, range_z, (x, y, z))


if __name__ == '__main__':
    droplet_map = {}
    max_x, max_y, max_z = 0, 0, 0
    with open('input.txt', 'r') as file:
        for line in file:
            x, y, z = map(lambda value: int(value) + 1, line.strip().split(','))
            if x not in droplet_map:
                droplet_map[x] = {}
            if y not in droplet_map[x]:
                droplet_map[x][y] = set()
            droplet_map[x][y].add(z)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            max_z = max(max_z, z)

    start = time.perf_counter()
    find_exterior_cubes(*get_cube_ranges(max_x, max_y, max_z))
    total_visible_sides = count_total_visible_sides(exterior_cubes)
    end = time.perf_counter()

    print(f'Tiempo de procesamiento: {end - start:.6f} segundos')
    print(f'El área total de los cubos de la gota de lava que están al descubierto es '
          f'{print_color(total_visible_sides, Color.RED)}.')
