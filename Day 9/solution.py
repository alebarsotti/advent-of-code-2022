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


def tail_should_move():
    head_x, head_y = head_position
    tail_x, tail_y = tail_position
    delta_x = abs(head_x - tail_x)
    delta_y = abs(head_y - tail_y)

    return delta_x > 1 or delta_y > 1


def move_tail():
    if not tail_should_move():
        return tail_position

    head_x, head_y = head_position
    tail_x, tail_y = tail_position
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


head_position = (0, 0)
tail_position = (0, 0)
visited_positions = set()
with open('input.txt', 'r') as file:
    for motion in file:
        direction, steps = motion.strip().split()
        steps = int(steps)
        for step in range(steps):
            head_position = movements[direction](head_position)
            tail_position = move_tail()
            visited_positions.add(tail_position)

print(f'La cantidad total de posiciones visitadas por la cola de la cuerda es '
      f'{print_color(len(visited_positions), Color.PURPLE)}')
