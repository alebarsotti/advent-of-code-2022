from Utils.Color import print_color, Color
import string

GROUP_SIZE = 3

items = list(string.ascii_lowercase) + list(string.ascii_uppercase)

total_priorities = 0
with open('input.txt', 'r') as file:
    lines = file.readlines()
    elves_groups = [lines[i:i + GROUP_SIZE] for i in range(0, len(lines), GROUP_SIZE)]
    for group in elves_groups:
        first, second, third = [x.strip() for x in group]
        repeated_element = [x for x in first if x in second and x in third][0]
        total_priorities += items.index(repeated_element) + 1

print(f'La suma de prioridades de los ítems repetidos en las mochilas de'
      f' grupos de 3 elfos es: {print_color(total_priorities, Color.CYAN)}')
