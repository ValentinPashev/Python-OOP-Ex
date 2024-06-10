# data = input().split()
# rows = int(data[0])
# columns = int(data[1])
#
#
# matrix = []
# counter = 0
#
# for row in range(rows):
#     matrix.append(input().split())
#
# for row_index in range(rows - 1):
#     for col in range(columns - 1):
#         if matrix[row_index][col] == matrix[row_index][col + 1] == matrix[row_index + 1][col] == matrix[row_index + 1][col + 1]:
#             counter += 1
#
# print(counter)
# ----------------------------------------------------------
# rows, cols = [int(x) for x in input().split()]
# matrix = []
# counter = 0
#
# for row in range(rows):
#     matrix.append(input().split())
#
# for row_index in range(rows - 1):
#     for col_index in range(cols - 1):
#         if matrix[row_index][col_index] == matrix[row_index + 1][col_index] == matrix[row_index][col_index + 1] ==\
#                 matrix[row_index + 1][col_index + 1]:
#             counter += 1
#
# print(counter)

rows, cols = [int(x) for x in input().split()]
matrix = [[str(x) for x in input().split()]for _ in range(rows)]
counter = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        if matrix[row_index][col_index] == matrix[row_index + 1][col_index] == matrix[row_index][col_index + 1] ==\
                matrix[row_index + 1][col_index + 1]:
            counter += 1


print(counter)