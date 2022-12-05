from Utils.Color import print_color, Color

stacks = {}
init_stacks = True
reading_stacks = True


def build_stacks():
    global init_stacks
    init_stacks = False
    stacks_count = len(line) // 4
    return {str(index + 1): [] for index in range(0, stacks_count)}


with open('input.txt', 'r') as file:
    for line in file:
        if init_stacks:
            stacks = build_stacks()

        if reading_stacks:
            char_list = [char for char in line]
            for stack_index, value_index in enumerate(range(1, len(char_list), 4)):
                stack_index = str(stack_index + 1)
                crate_id = char_list[value_index]
                if stack_index == crate_id:
                    reading_stacks = False
                    # Sort stacks
                    stacks = {key: value[::-1] for key, value in stacks.items()}
                    break
                if not crate_id.isspace():
                    stacks[stack_index].append(crate_id)
        elif line.startswith('move'):
            _, number_of_crates, _, stack_from, _, stack_to = line.strip().split()
            for x in range(int(number_of_crates)):
                stacks[stack_to].append(stacks[stack_from].pop())

crates_on_top = ''.join([value[-1] for value in stacks.values()])

print(f'Las cajas que quedan encima de cada pila son {print_color(crates_on_top, Color.GREEN)}.')
