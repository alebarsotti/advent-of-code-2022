from Utils.Color import print_color, Color

max_sum = 0
counter = 0
with open('input.txt', 'r') as file:
    for line in file:
        if line != '\n':
            counter += int(line)
        else:
            if max_sum < counter:
                max_sum = counter
            counter = 0

print(f'El elfo que tiene más calorías tiene un total de {print_color(max_sum, Color.RED)} calorías.')
