import functools
from ast import literal_eval
from Utils.Color import print_color, Color

divider_packet_1 = [[2]]
divider_packet_2 = [[6]]
packets = [divider_packet_1, divider_packet_2]
with open('input.txt', 'r') as file:
    for line in file:
        if not line.strip():
            continue
        packet = literal_eval(line.strip())
        packets.append(packet)


def compare_lists(left, right):
    left, right = fill_lists(left, right)
    for left_value, right_value in zip(left, right):
        if left_value is None:
            pair_is_ordered = True
        elif right_value is None:
            pair_is_ordered = False
        elif isinstance(left_value, int) and isinstance(right_value, int):
            pair_is_ordered = compare_ints(left_value, right_value)
        else:
            if not isinstance(left_value, list):
                left_value = [left_value]
            elif not isinstance(right_value, list):
                right_value = [right_value]

            pair_is_ordered = compare_lists(left_value, right_value)

        if pair_is_ordered is not None:
            return pair_is_ordered


def compare_ints(left, right):
    if left < right:
        return True
    elif right < left:
        return False
    return None


def fill_lists(left, right):
    if len(left) < len(right):
        left = left + [None] * (len(right) - len(left))
    elif len(right) < len(left):
        right = right + [None] * (len(left) - len(right))

    return left, right


def compare_packets(item_1, item_2):
    return -1 if compare_lists(item_1, item_2) else 1


packets.sort(key=functools.cmp_to_key(compare_packets))

divider_packet_1_index = packets.index(divider_packet_1) + 1
divider_packet_2_index = packets.index(divider_packet_2) + 1
decoder_key = divider_packet_1_index * divider_packet_2_index

print('La ubicación de los paquetes divisores es:')
print(f'\t- Paquete divisor 1: {print_color(divider_packet_1_index)}')
print(f'\t- Paquete divisor 2: {print_color(divider_packet_2_index)}')
print(f'\nLa clave de decodificación es: {print_color(decoder_key, Color.YELLOW)}')
