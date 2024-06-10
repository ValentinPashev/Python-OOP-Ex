# r, c = [int(x) for x in input().split()]
#
# start = ord('a')
#
# for rows in range(r):
#     for cols in range(c):
#         print(f"{chr(start + rows)}{chr(start + rows + cols)}{chr(start + rows)}", end=" ")
#     print()