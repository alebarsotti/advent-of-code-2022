from Utils.Color import print_color, Color

START = 0

END = 1


def is_overlapped_assignment(first, second):
    return contains(first, second[START]) or contains(first, second[END]) \
        or contains(second, first[START]) or contains(second, first[END])


def contains(section_range, value):
    return section_range[START] <= value <= section_range[END]


total_cases = 0
with open('input.txt', 'r') as file:
    for assignment_pair in file:
        section_ids_elf_1, section_ids_elf_2 = assignment_pair.strip().split(',')
        elf_1_range = tuple(int(x) for x in section_ids_elf_1.split('-'))
        elf_2_range = tuple(int(x) for x in section_ids_elf_2.split('-'))

        if is_overlapped_assignment(elf_1_range, elf_2_range):
            total_cases += 1

print(f'La cantidad de pares de asignaciones con solapamiento es {print_color(total_cases, Color.YELLOW)}.')
