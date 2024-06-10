# n = input().split(", ")
# rows = int(n[0])
# columns = int(n[1])
#
# matrix = []
# total_sum = 0
#
# for row_index in range(rows):
#     numbers = [int(el) for el in input().split(', ')]
#     matrix.append(numbers)
#     total_sum += sum(matrix[row_index])
#
# print(total_sum)
# print(matrix)
#
#
#


rows, cols = [int(x) for x in input().split(", ")]

matrix = []
total_sum = 0

for row in range(rows):
    sub_list = [int(x) for x in input().split(", ")]
    total_sum += sum(sub_list)
    matrix.append(sub_list)

print(total_sum)
print(matrix)