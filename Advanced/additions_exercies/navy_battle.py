a = 5
n = int(input())
position = None
matrix = []
mines = 0
cruisers = 0

for row in range(n):
    line = list(input())

    if "S" in line:
        position = ([row, line.index("S")])

    if "*" in line:
        mines += line.count("C")

    if "C" in line:
        cruisers += line.count("C")

    matrix.append(line)

sub_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

sub_direction = input()

while mines != 0 and cruisers != 0:
    current_row, current_col = position
    next_row, next_col = sub_directions[sub_direction]
    desired_row = current_row + next_row
    desired_col = current_col + next_col

    # Next position:
    current_symbol = matrix[desired_row][desired_col]

    if current_symbol == "-":
        matrix[current_row][current_col] = "-"
        matrix[desired_row][desired_col] = "S"
        position = [desired_row, desired_col]

    if current_symbol == "*":
        mines -= 1
        matrix[current_row][current_col] = "-"
        matrix[desired_row][desired_col] = "S"
        position = [desired_row, desired_col]

        if mines == 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{desired_row}, {desired_col}]!")
            for row in matrix:
                print(f"".join(row))
            break

    elif current_symbol == "C":
        cruisers -= 1
        matrix[current_row][current_col] = "-"
        matrix[desired_row][desired_col] = "S"
        position = [desired_row, desired_col]

        if cruisers == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            for row in matrix:
                print(f"".join(row))

            break

    sub_direction = input()
