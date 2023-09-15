# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

n_rows = int(input("How many rows by the tree? "))
n_stars = 1
n_spaces = n_rows - 1

for i_row in range(n_rows):
    row_str = ' ' * n_spaces
    n_spaces -= 1
    row_str += '*' * n_stars
    n_stars += 2
    print(row_str)

