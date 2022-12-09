from Utils.Color import print_color, Color


forest = []
with open('input.txt', 'r') as file:
    for line in file:
        forest.append([int(x) for x in line.strip()])


def is_edge_tree(tree_row_index, tree_col_index, row):
    return tree_row_index == 0 or tree_col_index == 0 or tree_col_index == len(row) - 1 or tree_row_index == len(forest) - 1


def check_top_visibility(tree_row_index, tree_col_index, tree):
    for row_index in range(tree_row_index):
        if forest[row_index][tree_col_index] >= tree:
            return False
    return True


def check_bottom_visibility(tree_row_index, tree_col_index, tree):
    for row_index in range(tree_row_index + 1, len(forest)):
        if forest[row_index][tree_col_index] >= tree:
            return False
    return True


def check_left_visibility(tree_row_index, tree_col_index, tree):
    for col_index in range(tree_col_index):
        if forest[tree_row_index][col_index] >= tree:
            return False
    return True


def check_right_visibility(tree_row_index, tree_col_index, tree):
    for col_index in range(tree_col_index + 1, len(forest[0])):
        if forest[tree_row_index][col_index] >= tree:
            return False
    return True


def check_tree_visibility(tree_row_index, tree_col_index, tree):
    return check_left_visibility(tree_row_index, tree_col_index, tree) \
        or check_right_visibility(tree_row_index, tree_col_index, tree) \
        or check_top_visibility(tree_row_index, tree_col_index, tree) \
        or check_bottom_visibility(tree_row_index, tree_col_index, tree)


visible_trees_count = 0
for tree_row_index, row in enumerate(forest):
    for tree_col_index, tree in enumerate(row):
        if is_edge_tree(tree_row_index, tree_col_index, row):
            visible_trees_count += 1
        elif check_tree_visibility(tree_row_index, tree_col_index, tree):
            visible_trees_count += 1

print(f'\nLa cantidad de árboles visibles desde afuera es {print_color(visible_trees_count, Color.GREEN)}')
