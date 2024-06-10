# rows = int(input())
#
# matrix = []
#
# for row in range(rows):
#     numbers = [int(el) for el in input().split(', ')]
#     matrix.append(numbers)
#
# even_matrix = []
#
# for row_index in range(rows):
#     even_matrix.append([])
#     for col in range(len(matrix[row_index])):
#         even_number = matrix[row_index][col]
#         if even_number % 2 == 0:
#             even_matrix[row_index].append(even_number)
#
# print(even_matrix)

rows = int(input())
matrix = []

for row in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    even_matrix = [int(num) for num in numbers if num % 2 == 0]
    matrix.append(even_matrix)

print(matrix)
