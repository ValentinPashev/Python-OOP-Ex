# n = int(input())
#
# matrix = []
#
# for rows in range(n):
#     numbers = [int(el) for el in input().split(', ')]
#     matrix.append(numbers)
#
# flattened = []
#
# for row_index in range(n):
#     for col_index in range(len(matrix[row_index])):
#         flattened.append(matrix[row_index][col_index])
#
# print(flattened)


rows = int(input())
flatten_matrix = []

for row in range(rows):
    number = [int(x) for x in input().split(", ")]

    for num in number:
        flatten_matrix.append(num)

print(flatten_matrix)