rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([el for el in input()])

symbol = input()
occ = []

for row_index in range(rows):
    for col in range(rows):
        if matrix[row_index][col] == symbol:
            occ.append(row_index)
            occ.append(col)
            break

if occ:
    print(f"({occ[0]}, {occ[1]})")

else:
    print(f"{symbol} does not occur in the matrix")