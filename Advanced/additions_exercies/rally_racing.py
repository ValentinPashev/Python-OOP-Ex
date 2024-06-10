n = int(input())
race_car_number = input()
tunel_locations = []
kilometers_passed = 0
matrix = []
my_position = (0, 0)


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    data = list(input().split())

    if "T" in data:
        tunel_locations.append([row, data.index("T")])
    matrix.append(data)

command = input()

while command != "End":
    current_row, current_col = my_position
    next_row, next_col = direction_mapper[command]
    desired_row = current_row + next_row
    desired_col = current_col + next_col
    my_position = desired_row, desired_col
    current_symbol = matrix[desired_row][desired_col]

    if current_symbol == ".":
        kilometers_passed += 10
        matrix[desired_row][desired_col] = "C"
        matrix[current_row][current_col] = "."

    elif current_symbol == "T":
        kilometers_passed += 30
        row_of_tunel = tunel_locations[1][0]
        col_of_tunel = tunel_locations[1][1]
        row_to_del = tunel_locations[0][0]
        col_to_del = tunel_locations[0][1]
        matrix[row_to_del][col_to_del] = "."
        my_position = row_of_tunel, col_of_tunel
        matrix[current_row][current_col] = "."
        matrix[row_of_tunel][col_of_tunel] = "C"

    elif current_symbol == "F":
        matrix[desired_row][desired_col] = "C"
        matrix[current_row][current_col] = "."
        kilometers_passed += 10
        print(f"Racing car {race_car_number} finished the stage!")
        print(f"Distance covered {kilometers_passed} km.")
        for row in matrix:
            print(f"".join(row))
        exit()

    command = input()

else:
    print(f"Racing car {race_car_number} DNF.")
    print(f'Distance covered {kilometers_passed} km.')
for row in matrix:
    print(f"".join(row))
