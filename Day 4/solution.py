from Utils.Color import print_color, Color

END = 1

START = 0


def is_fully_contained_assignment(first_range, second_range):
    return contains(first_range, second_range) or contains(second_range, first_range)


def contains(first_range, second_range):
    return second_range[START] >= first_range[START] and second_range[END] <= first_range[END]


total_cases = 0
with open('input.txt', 'r') as file:
    for assignment_pair in file:
        section_ids_elf_1, section_ids_elf_2 = assignment_pair.strip().split(',')
        elf_1_range = tuple(int(x) for x in section_ids_elf_1.split('-'))
        elf_2_range = tuple(int(x) for x in section_ids_elf_2.split('-'))

        if is_fully_contained_assignment(elf_1_range, elf_2_range):
            total_cases += 1

print(f'La cantidad de pares de asignaciones en las cuales un rango '
      f'contiene completamente al otro es {print_color(total_cases, Color.YELLOW)}.')
