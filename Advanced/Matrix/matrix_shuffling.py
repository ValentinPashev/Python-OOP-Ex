# def are_coordinates_valid(r1, c1, r2, c2, num_rows, num_cols):
#     return 0 <= r1 < num_rows and 0 <= r2 < num_rows and 0 <= c1 < num_cols and 0 <= c2 < num_cols
#
#
# rows, columns = [int(x) for x in input().split()]
# matrix = [[x for x in input().split()] for _ in range(rows)]
#
# while True:
#     line = input()
#
#     if line == "END":
#         break
#
#     command = line.split()
#
#     if command[0] != "swap" or len(command) != 5:
#         print(f'Invalid input!')
#         continue
#
#     row1, col1, row2, col2 = [int(x) for x in command[1:]]
#
#     if are_coordinates_valid(row1, col1, row2, col2, rows, columns):
#         matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#         [print(*row_line) for row_line in matrix]
#
#     else:
#         print(f'Invalid input!')

def valid_indices(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def swap_elements(command, indices):
    if len(indices) == 4 and valid_indices(indices) and command == "swap":
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        [print(*row) for row in matrix]

    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == "END":
        break

    swap_elements(command_type, coordinates)
