from Utils.Color import print_color, Color
from Utils.Timer import timed_method

ROOT_MONKEY = 'root'

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}


def read_monkeys():
    with open('input.txt', 'r') as file:
        number_monkeys = {}
        operation_monkeys = {}
        for line in file:
            name, value = map(str.strip, line.split(':'))
            if value.isdigit():
                number_monkeys[name] = int(value)
            else:
                operation_monkeys[name] = value

        return number_monkeys, operation_monkeys


def solve_operation(value: str, number_monkeys: dict):
    operand_one, operation, operand_two = value.split()
    operand_one = number_monkeys.get(operand_one)
    operand_two = number_monkeys.get(operand_two)
    if not operand_one or not operand_two:
        return None

    return operations[operation](operand_one, operand_two)


def solve_operation_monkeys(number_monkeys: dict, operation_monkeys: dict):
    while operation_monkeys:
        for name in list(operation_monkeys):
            value = operation_monkeys[name]
            result = solve_operation(value, number_monkeys)
            if result:
                number_monkeys[name] = result
                operation_monkeys.pop(name)

    return number_monkeys


@timed_method
def main():
    number_monkeys, operation_monkeys = read_monkeys()
    monkeys = solve_operation_monkeys(number_monkeys, operation_monkeys)
    root_value = monkeys[ROOT_MONKEY]
    print(f'El valor que grita el mono "{ROOT_MONKEY}" es {print_color(root_value, Color.YELLOW)}.')


if __name__ == '__main__':
    main()
