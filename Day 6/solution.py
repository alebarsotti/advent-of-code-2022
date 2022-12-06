from Utils.Color import print_color, Color

MARKER_SIZE = 4

with open('input.txt', 'r') as file:
    for line in file:
        for last_letter_index in range(MARKER_SIZE - 1, len(line)):
            last_letter_index += 1
            packet_marker = line[last_letter_index - MARKER_SIZE:last_letter_index]
            if len(packet_marker) == len(set(packet_marker)):
                print(f'La cantidad de caracteres que necesitan ser procesados antes del primer'
                      f'marcador de paquetes es {print_color(last_letter_index, Color.LIGHT_CYAN)}.')
                break
