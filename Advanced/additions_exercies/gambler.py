def is_next_position_valid(row_index, col_index, n):
    return 0 <= row_index < n and 0 <= col_index < n

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

n = int(input())
gambler_position = None
matrix = []

for row in range(n):
    data = list(input())

    if "G" in data:
        gambler_position = [row, data.index("G")]

    matrix.append(data)

command = input()


money = 100

while command != "end":

    current_row, current_col = gambler_position
    row_movement, col_movement = direction_mapper[command]
    desired_row = current_row + row_movement
    desired_col = current_col + col_movement

    if not is_next_position_valid(desired_row, desired_col, n):
        print("Game over! You lost everything!")
        exit()

    current_symbol = matrix[desired_row][desired_col]
    matrix[desired_row][desired_col] = "G"
    matrix[current_row][current_col] = "-"
    gambler_position = [desired_row, desired_col]

    if current_symbol == "W":
        money += 100

    elif current_symbol == "P":
        money -= 200
        if money <= 0:
            money = 0
            print("Game over! You lost everything!")
            exit()

    elif current_symbol == "J":
        money += 100000
        print(f"You win the Jackpot!")
        print(f"End of the game. Total amount: {money}$")
        for row in matrix:
            print(f''.join(row))
        exit()

    command = input()

print(f"End of the game. Total amount: {money}$")
for row in matrix:
    print(f''.join(row))