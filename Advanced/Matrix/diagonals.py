# n = int(input())
# matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
#
# primary_matrix = [matrix[i][i] for i in range(n)]
# secondary_matrix = [matrix[i][n - i - 1] for i in range(n)]
#
# print(f"Primary diagonal: {', '.join([str(x) for x in primary_matrix])}. Sum: {sum(primary_matrix)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_matrix])}. Sum: {sum(secondary_matrix)}")

# -------------------------------------------------------------------------
#
# rows = int(input())
#
# matrix = [[int(x) for x in input().split(", ")]for _ in range(rows)]
#
# primary_diagonal = [matrix[i][i] for i in range(rows)]
# secondary_diagonal = [matrix[i][rows - i - 1] for i in range(rows)]
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

# ---------------------------------------------------------------------------

rows = int(input())

matrix = []

primary_diagonal = []
secondary_diagonal = []


for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][rows - i - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
