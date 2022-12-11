from Utils.Color import print_color, Color

ADDX_CYCLE_DURATION = 2
SCREEN_WIDTH = 40
LIT_PIXEL = '#'
DARK_PIXEL = '.'


def is_addx(ins):
    return ins[0] == 'addx'


current_cycle = 0
x_register = 1
current_row = ''
screen_rows = []


def get_pixel_type(current_pixel, sprite_position):
    return LIT_PIXEL if current_pixel in sprite_position else DARK_PIXEL


def get_sprite_position(sprite_center_pixel_position):
    return [sprite_center_pixel_position - 1, sprite_center_pixel_position, sprite_center_pixel_position + 1]


def increment_cycle():
    global current_cycle, current_row, x_register

    current_pixel = current_cycle % SCREEN_WIDTH
    current_row += get_pixel_type(current_pixel, get_sprite_position(x_register))

    insert_line_break()

    current_cycle += 1


def insert_line_break():
    global current_row
    if len(current_row) == SCREEN_WIDTH:
        screen_rows.append(current_row)
        current_row = ''


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

print('Salida del programa:')
for row in screen_rows:
    for char in row:
        print(print_color(char, Color.ORANGE) if char == LIT_PIXEL else print_color(char, Color.LIGHT_GRAY), end='')
    print()

print(f'Las letras dibujadas en la pantalla por el programa son {print_color("EHPZPJGL", Color.ORANGE)}')
