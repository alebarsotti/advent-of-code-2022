from Utils.Color import print_color, Color


forest = []
with open('input.txt', 'r') as file:
    for line in file:
        forest.append([int(x) for x in line.strip()])


def is_edge_tree(tree_row_index, tree_col_index, row):
    return tree_row_index == 0 or tree_col_index == 0 or tree_col_index == len(row) - 1 or tree_row_index == len(forest) - 1


def calculate_top_viewing_distance(tree_row_index, tree_col_index, tree):
    viewing_distance = 0
    for row_index in reversed(range(tree_row_index)):
        viewing_distance += 1
        adjacent_tree = forest[row_index][tree_col_index]
        if adjacent_tree >= tree:
            break
    return viewing_distance


def calculate_bottom_viewing_distance(tree_row_index, tree_col_index, tree):
    viewing_distance = 0
    for row_index in range(tree_row_index + 1, len(forest)):
        viewing_distance += 1
        adjacent_tree = forest[row_index][tree_col_index]
        if adjacent_tree >= tree:
            break
    return viewing_distance


def calculate_left_viewing_distance(tree_row_index, tree_col_index, tree):
    viewing_distance = 0
    for col_index in reversed(range(tree_col_index)):
        viewing_distance += 1
        adjacent_tree = forest[tree_row_index][col_index]
        if adjacent_tree >= tree:
            break
    return viewing_distance


def calculate_right_viewing_distance(tree_row_index, tree_col_index, tree):
    viewing_distance = 0
    for col_index in range(tree_col_index + 1, len(forest[0])):
        viewing_distance += 1
        adjacent_tree = forest[tree_row_index][col_index]
        if adjacent_tree >= tree:
            break
    return viewing_distance


def calculate_tree_scenic_score(tree_row_index, tree_col_index, tree):
    return calculate_left_viewing_distance(tree_row_index, tree_col_index, tree)\
        * calculate_right_viewing_distance(tree_row_index, tree_col_index, tree)\
        * calculate_top_viewing_distance(tree_row_index, tree_col_index, tree)\
        * calculate_bottom_viewing_distance(tree_row_index, tree_col_index, tree)


max_scenic_score = 0
for tree_row_index, row in enumerate(forest):
    for tree_col_index, tree in enumerate(row):
        if is_edge_tree(tree_row_index, tree_col_index, row):
            continue
        else:
            scenic_score = calculate_tree_scenic_score(tree_row_index, tree_col_index, tree)
            max_scenic_score = max(max_scenic_score, scenic_score)

print(f'\nEl puntaje escénico más alto es {print_color(max_scenic_score, Color.GREEN)}')
