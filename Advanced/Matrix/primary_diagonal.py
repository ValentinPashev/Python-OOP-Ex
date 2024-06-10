rows = int(input())
matrix = []

for row in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

total_sum = 0

for row_index in range(rows):
    for col_index in range(rows):
        if row_index == col_index:
            total_sum += matrix[row_index][col_index]

print(total_sum)


# rows = int(input())
# matrix = []
# index = 0
# total_sum = 0

# for row in range(rows):
#     numbers = [int(x) for x in input().split()]
#      total_sum += numbers[index]
#     index += 1
#     matrix.append(numbers)
#
# print(total_sum)