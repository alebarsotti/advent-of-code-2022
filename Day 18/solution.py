import time

from Utils.Color import print_color, Color

DROPLET_SIDES = 6

droplet_map = {}
with open('input.txt', 'r') as file:
    for line in file:
        x, y, z = map(int, line.strip().split(','))
        if x not in droplet_map:
            droplet_map[x] = {}
        if y not in droplet_map[x]:
            droplet_map[x][y] = set()
        droplet_map[x][y].add(z)


def get_adjacent_cubes_count(x, y, z):
    count = 0
    count += z in droplet_map.get(x + 1, {}).get(y, ())
    count += z in droplet_map.get(x - 1, {}).get(y, ())
    count += z in droplet_map.get(x, {}).get(y + 1, ())
    count += z in droplet_map.get(x, {}).get(y - 1, ())
    count += z + 1 in droplet_map.get(x, {}).get(y, ())
    count += z - 1 in droplet_map.get(x, {}).get(y, ())
    return count


total_visible_sides = 0
start = time.perf_counter()
for x, y_dict in droplet_map.items():
    for y, z_set in y_dict.items():
        for z in z_set:
            adjacent_droplets_count = get_adjacent_cubes_count(x, y, z)
            total_visible_sides += DROPLET_SIDES - adjacent_droplets_count
end = time.perf_counter()

print(f'Tiempo de procesamiento: {end - start:.6f} segundos')
print(f'El área total de los cubos de la gota de lava que están al descubierto es '
      f'{print_color(total_visible_sides, Color.RED)}.')
