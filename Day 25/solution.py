from Utils.Color import print_color, Color
from Utils.Timer import timed_method

BASE_NUMBER = 5

digit_values = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

test = [1747, 906, 198, 11, 201, 31, 1257, 32, 353, 107, 7, 3, 37]


def read_numbers():
    with open('input.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def convert_numbers(numbers):
    converted_numbers = []
    for number in numbers:
        number_value = 0
        for power, digit in enumerate(reversed(number)):
            digit_value = digit_values[digit]
            digit_result = digit_value * BASE_NUMBER ** power
            number_value += digit_result

        converted_numbers.append(number_value)

    return converted_numbers


def get_max_snafu_power(number):
    power = -1
    number_representation_acc = 0
    while number_representation_acc < number:
        power += 1
        number_representation_acc += 2 * BASE_NUMBER ** power
    return power


def convert_to_snafu(number):
    snafu_number = ''
    power = get_max_snafu_power(number)
    accumulated_value = 0
    for power in reversed(range(power + 1)):
        difference = accumulated_value - number
        # Get digit that reduces the absolute value of the difference to the minimum possible.
        digit = min(digit_values, key=lambda k: abs(difference + digit_values[k] * BASE_NUMBER ** power))
        # Add digit to SNAFU number.
        snafu_number += digit
        # Update accumulated value of the found digits.
        accumulated_value += digit_values[digit] * BASE_NUMBER ** power

    return snafu_number


@timed_method
def main():
    numbers = read_numbers()

    converted_numbers = convert_numbers(numbers)

    total_fuel_requirements = sum(converted_numbers)

    snafu_value = convert_to_snafu(total_fuel_requirements)

    print(f'La cantidad total de combustible que será procesado es {print_color(total_fuel_requirements, Color.CYAN)}')
    print(f'El número SNAFU que debe ingresarse en la consola de Bob es {print_color(snafu_value, Color.CYAN)}')


if __name__ == '__main__':
    main()
