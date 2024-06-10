n = int(input())
bombs_direction_count = int(input())

minesweep = [[0 for col in range(n)]for row in range(n)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'up_right': (-1, 1),
    'down_right': (1, 1),
    'down_left': (1, -1),
    'up_left': (-1, -1)
}

for _ in range(bombs_direction_count):
    position = input()
    tuple_output = tuple(map(int, position.strip("()").split(", ")))
    r = int(tuple_output[0])
    c = int(tuple_output[1])
    minesweep[r][c] = "*"


for row_index in range(n):
    for col_index in range(n):
        if minesweep[row_index][col_index] == "*":
            for value in directions.values():
                new_row = value[0]
                new_col = value[1]
                desired_row = row_index - new_row
                desired_col = col_index - new_col
                if 0 <= desired_row < n and 0 <= desired_col < n:
                    if minesweep[desired_row][desired_col] == "*":
                        continue

                    minesweep[desired_row][desired_col] += 1


for row in minesweep:
    print(*row, end="\n")

