from Utils.Color import Color, print_color

sum_list = []
counter = 0
with open('input.txt', 'r') as file:
    for line in file:
        if line != '\n':
            counter += int(line)
        else:
            sum_list.append(counter)
            counter = 0

# Sort in descending order
sum_list.sort(reverse=True)
top_3_calories = sum_list[:3]
total_calories = sum(top_3_calories)
print(f'Los tres elfos que tienen más calorías tienen estos valores: {print_color(top_3_calories, Color.RED)}.')
print(f'En total, los tres elfos que más calorías '
      f'tienen suman {print_color(total_calories, Color.RED)} calorías.')
