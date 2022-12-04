from Utils.Color import print_color, Color
import string

item_types = list(string.ascii_lowercase) + list(string.ascii_uppercase)

total_priorities = 0
with open('input.txt', 'r') as file:
    for rucksack in file:
        rucksack = rucksack.strip()
        middle = int(len(rucksack) / 2)
        first_compartment = rucksack[:middle]
        second_compartment = rucksack[middle:]

        repeated_element = [x for x in first_compartment if x in second_compartment][0]
        total_priorities += item_types.index(repeated_element) + 1

print(f'La suma de prioridades de los ítems repetidos en ambos '
      f'compartimentos de cada mochila es : {print_color(total_priorities, Color.CYAN)}.')
