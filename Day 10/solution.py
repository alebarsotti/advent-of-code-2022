from Utils.Color import print_color, Color

ADDX_CYCLE_DURATION = 2
CYCLE_SPAN = 40


def is_addx(ins):
    return ins[0] == 'addx'


current_cycle = 0
next_cycle_checkpoint = 20
x_register = 1
signal_strength = 0


def increment_cycle():
    global current_cycle, next_cycle_checkpoint, signal_strength

    current_cycle += 1
    check_signal_strength()


def check_signal_strength():
    global current_cycle, next_cycle_checkpoint, signal_strength

    if current_cycle == next_cycle_checkpoint:
        next_cycle_checkpoint += CYCLE_SPAN
        signal_strength += current_cycle * x_register


with open('input.txt', 'r') as file:
    for instruction in file:
        instruction = instruction.strip().split()
        if is_addx(instruction):
            _, delta_value = instruction
            for i in range(ADDX_CYCLE_DURATION):
                increment_cycle()
            x_register += int(delta_value)
        else:
            increment_cycle()

print(f'La suma de las intensidades de señal es {print_color(signal_strength, Color.ORANGE)}')
