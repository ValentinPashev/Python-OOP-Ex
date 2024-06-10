# n = int(input())
# matrix = [[int(x) for x in input().split(" ")] for _ in range(n)]
#
# primary_matrix = [matrix[i][i] for i in range(n)]
# secondary_matrix = [matrix[i][n - i - 1] for i in range(n)]
#
# total_sum = abs(sum(primary_matrix) - sum(secondary_matrix))
#
# print(total_sum)

rows = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(rows)]

primary_matrix = [matrix[i][i] for i in range(rows)]
secondary_matrix = [matrix[i][rows - i - 1] for i in range(rows)]

total_sum = sum(primary_matrix) - sum(secondary_matrix)

print(abs(total_sum))