from Utils.Color import print_color, Color

RIGHT = 'R'
LEFT = 'L'
UP = 'U'
DOWN = 'D'

movements = {
    RIGHT: lambda position: (position[0] + 1, position[1]),
    LEFT: lambda position: (position[0] - 1, position[1]),
    UP: lambda position: (position[0], position[1] + 1),
    DOWN: lambda position: (position[0], position[1] - 1)
}


def part_should_move(head_part, tail_part):
    head_x, head_y = head_part
    tail_x, tail_y = tail_part
    delta_x = abs(head_x - tail_x)
    delta_y = abs(head_y - tail_y)

    return delta_x > 1 or delta_y > 1


def move_part(head_part, tail_part):
    if not part_should_move(head_part, tail_part):
        return tail_part

    head_x, head_y = head_part
    tail_x, tail_y = tail_part
    delta_x = abs(head_x - tail_x)
    delta_y = abs(head_y - tail_y)

    if delta_x > 1 and delta_y == 0:
        return (head_x + tail_x) // 2, tail_y
    elif delta_y > 1 and delta_x == 0:
        return tail_x, (head_y + tail_y) // 2
    elif delta_x > 1 and delta_y == 1:
        return (head_x + tail_x) // 2, head_y
    elif delta_y > 1 and delta_x == 1:
        return head_x, (head_y + tail_y) // 2
    else:
        return (head_x + tail_x) // 2, (head_y + tail_y) // 2


rope = [(0, 0)] * 10
visited_positions = set()
with open('input.txt', 'r') as file:
    for motion in file:
        direction, steps = motion.strip().split()
        for step in range(int(steps)):
            rope[0] = movements[direction](rope[0])
            for index in range(len(rope)):
                if index < len(rope) - 1:
                    rope[index + 1] = move_part(rope[index], rope[index + 1])
            visited_positions.add(rope[9])

print(f'La cantidad total de posiciones visitadas por la cola de la cuerda es '
      f'{print_color(len(visited_positions), Color.PURPLE)}')
