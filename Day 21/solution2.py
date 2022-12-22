import re
import time

from sympy import sympify, solve

from Utils.Color import print_color, Color

ROOT_MONKEY = 'root'
HUMAN_MONKEY = 'humn'
SYMBOL = 'x'
EQUALS = '='

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
    '=': lambda a, b: a == b,
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
                value = str.replace(value, HUMAN_MONKEY, SYMBOL)
                operation_monkeys[name] = value
        # Replace value of Human monkey
        number_monkeys[HUMAN_MONKEY] = SYMBOL
        # Replace value of Root monkey
        operand_one, _, operand_two = operation_monkeys[ROOT_MONKEY].split()
        operation_monkeys[ROOT_MONKEY] = f'{operand_one} = {operand_two}'

        return number_monkeys, operation_monkeys


def solve_operation(value: str, number_monkeys: dict):
    operand_one, operation, operand_two = value.split()
    operand_one_value = number_monkeys.get(operand_one)
    operand_two_value = number_monkeys.get(operand_two)
    if operand_one == SYMBOL:
        return f'{operand_one} {operation} {operand_two_value if operand_two_value else operand_two}'
    elif operand_two == SYMBOL:
        return f'{operand_one_value if operand_one_value else operand_one} {operation} {operand_two}'
    elif not operand_one_value or not operand_two_value:
        return None
    elif not str(operand_one_value).isdigit() or not str(operand_two_value).isdigit():
        return f'({operand_one_value}) {operation} ({operand_two_value})'

    return operations[operation](operand_one_value, operand_two_value)


def solve_operation_monkeys(number_monkeys: dict, operation_monkeys: dict):
    while operation_monkeys:
        for name in list(operation_monkeys):
            value = operation_monkeys[name]
            result = solve_operation(value, number_monkeys)
            if len(re.findall(r'[a-z]+', str(result))) > 1:
                operation_monkeys[name] = result
            elif result:
                number_monkeys[name] = result
                operation_monkeys.pop(name)

    return number_monkeys


def solve_equation(equation):
    equation = sympify(f'Eq({str.replace(equation, EQUALS, ",")})')

    return solve(equation)[0]


if __name__ == '__main__':
    start = time.perf_counter()

    number_monkeys, operation_monkeys = read_monkeys()

    monkeys = solve_operation_monkeys(number_monkeys, operation_monkeys)

    result = solve_equation(monkeys[ROOT_MONKEY])

    end = time.perf_counter()
    print(f'Tiempo de procesamiento: {end - start:.6f} segundos')
    print(f'El valor que el humano debe gritar para que el test del mono "{ROOT_MONKEY}" sea exitoso es '
          f'{print_color(result, Color.YELLOW)}.')
