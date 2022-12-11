import math

from Utils.Color import print_color, Color


class Instruction:
    MONKEY = "Monkey"
    STARTING_ITEMS = "Starting"
    OPERATION = "Operation"
    TEST = "Test"
    IF = "If"
    TRUE = "true"
    FALSE = "false"


class Monkey:
    def __init__(self, monkey_id):
        self.id = monkey_id
        self.items = None
        self.dividend = None
        self.operation = None
        self.test_true_monkey_id = None
        self.test_false_monkey_id = None
        self.inspection_count = 0

    def inspect(self):
        global lcm
        self.inspection_count += 1
        item = self.items.pop(0)
        operation = self.operation.replace('old', str(item))
        return eval(operation) % lcm

    def test_item(self, item):
        return self.test_true_monkey_id if item % self.dividend == 0 else self.test_false_monkey_id

    def __str__(self):
        return f'\nMonkey {self.id}' \
               f'\n\tItems: {self.items}' \
               f'\n\tOperation: {self.operation}' \
               f'\n\tDivided: {self.dividend}' \
               f'\n\tTest true: {self.test_true_monkey_id}' \
               f'\n\tTest false: {self.test_false_monkey_id}' \
               f'\n\tInspection count: {self.inspection_count}'

    def __repr__(self):
        return self.__str__()


def throw_item_to_monkey(item, monkey_id):
    next(filter(lambda x: x.id == monkey_id, monkies)).items.append(item)


current_monkey = None
lcm = 0
monkies = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip().replace(',', '').replace(':', '').split()
        if not line:
            continue

        match line[0]:
            case Instruction.MONKEY:
                current_monkey = Monkey(monkey_id=line[1])
            case Instruction.STARTING_ITEMS:
                current_monkey.items = [int(x) for x in line if x.isdecimal()]
            case Instruction.OPERATION:
                current_monkey.operation = ' '.join(line[line.index("=") + 1:])
            case Instruction.TEST:
                current_monkey.dividend = int(line[-1])
            case Instruction.IF:
                if line[1] == Instruction.TRUE:
                    current_monkey.test_true_monkey_id = line[-1]
                else:
                    current_monkey.test_false_monkey_id = line[-1]
                    monkies.append(current_monkey)

lcm = math.lcm(*[x.dividend for x in monkies])

for round_number in range(10_000):
    for monkey in monkies:
        for item_index in range(len(monkey.items)):
            item = monkey.inspect()
            monkey_id_to_pass_item = monkey.test_item(item)
            throw_item_to_monkey(item, monkey_id_to_pass_item)

monkies.sort(key=lambda x: x.inspection_count, reverse=True)
result = math.prod([x.inspection_count for x in monkies[:2]])
print(f'El nivel de monkey business es {print_color(result, Color.BLUE)}')
