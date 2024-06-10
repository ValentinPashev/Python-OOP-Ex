def is_index_valid(row_index, col_index, n):
    return 0 <= row_index < n and 0 <= col_index < n


n = int(input())
snake_position = None
lairs = []
food = 0
food_count = 0

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
snake_hole = []

for row in range(n):
    line = list(input())

    if "S" in line:
        snake_position = (row, line.index("S"))

    if "B" in line:
        lairs.append([row, line.index("B")])

    if "*" in line:
        food_count += line.count('*')

    snake_hole.append(line)


while food != 10:
    command = input()
    current_row, current_col = snake_position
    next_row, next_col = direction_mapper[command]
    desired_row = current_row + next_row
    desired_col = current_col + next_col

    if not is_index_valid(desired_row, desired_col, n):
        last_row, last_col = snake_position
        snake_hole[last_row][last_col] = '.'
        print("Game over!")
        print(f"Food eaten: {food}")
        for row in snake_hole:
            print(f''.join(row))
        exit()

    current_symbol = snake_hole[desired_row][desired_col]
    snake_hole[desired_row][desired_col] = "S"
    snake_hole[current_row][current_col] = "."
    snake_position = [desired_row, desired_col]

    if current_symbol == "*":
        food += 1

    elif current_symbol == "B":
        snake_hole[desired_row][desired_col] = '.'
        current_position = lairs[1]
        r = current_position[0]
        c = current_position[1]

        snake_position = [r, c]

if food == 10:
    print(f"You won! You fed the snake.")
    print(f"Food eaten: {food}")

for row in snake_hole:
    print(f''.join(row))

