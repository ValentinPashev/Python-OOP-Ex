# data = input().split(", ")
# rows = int(data[0])
# columns = int(data[1])
#
#
# matrix = []
#
# total_sum = 0
#
# for row in range(rows):
#     numbers = [int(el) for el in input().split()]
#     matrix.append(numbers)
#
# for col_index in range(columns):
#     total_sum = 0
#     for row_index in range(rows):
#         total_sum += matrix[row_index][col_index]
#     print(total_sum)


rows, cols = [int(x) for x in input().split(", ")]
matrix = []


for row in range(rows):
    number = [int(x) for x in input().split()]
    matrix.append(number)

for col_index in range(cols):
    total_sum = 0
    for row_index in range(rows):
        total_sum += matrix[row_index][col_index]
    print(total_sum)