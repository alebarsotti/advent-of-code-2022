from ast import literal_eval
from Utils.Color import print_color, Color

packets_pairs = []
with open('input.txt', 'r') as file:
    left_packet = None
    for line in file:
        if not line.strip():
            continue
        packet = literal_eval(line.strip())
        if left_packet is None:
            left_packet = packet
        else:
            packets_pairs.append((left_packet, packet))
            left_packet = None


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
        left.extend([None] * (len(right) - len(left)))
    elif len(right) < len(left):
        right.extend([None] * (len(left) - len(right)))

    return left, right


sum_ordered_packets_indexes = 0
for packet_index, (left_packet, right_packet) in enumerate(packets_pairs):
    is_ordered = compare_lists(left_packet, right_packet)
    if is_ordered:
        sum_ordered_packets_indexes += packet_index + 1

print(f'La suma de los índices de los paquetes que se encuentran ordenados es '
      f'{print_color(sum_ordered_packets_indexes, Color.YELLOW)}')
