n = int(input())
position = None
matrix = []
initial_armor = 300
enemy_planes = 0

jet_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    airspace = list(input())

    if "J" in airspace:
        position = (row, airspace.index("J"))
    if "E" in airspace:
        enemy_planes += airspace.count("E")


    matrix.append(airspace)

command = input()

while command:
    current_row, current_col = position
    next_row, next_col = jet_directions[command]
    desired_row = current_row + next_row
    desired_col = current_col + next_col

    current_symbol = matrix[desired_row][desired_col]

    if current_symbol == "-":
        matrix[current_row][current_col] = "-"
        matrix[desired_row][desired_col] = "J"
        position = [desired_row, desired_col]

    elif current_symbol == "E":
        matrix[current_row][current_col] = "-"
        matrix[desired_row][desired_col] = "J"
        position = [desired_row, desired_col]
        enemy_planes -= 1

        if enemy_planes == 0:
            print(f"Mission accomplished, you neutralized the aerial threat!")
            for row in matrix:
                print(f"".join(row))
            exit()
        else:
            initial_armor -= 100

    elif current_symbol == "R":
        matrix[current_row][current_col] = "-"
        matrix[desired_row][desired_col] = "J"
        position = [desired_row, desired_col]
        initial_armor = 300

    if initial_armor == 0:
        position = [desired_row, desired_col]
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{position[0]}, {position[1]}]!")
        for row in matrix:
            print(f"".join(row))

        exit()

    command = input()

if enemy_planes == 1:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{position[0]}, {position[1]}]!")
    for row in matrix:
        print(f"".join(row))

        exit()
