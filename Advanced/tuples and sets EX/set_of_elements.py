first_number, second_number = input().split()

first_set = set()
second_set = set()

for _ in range(int(first_number)):
    num = int(input())
    first_set.add(num)

for j in range(int(second_number)):
    second_num = int(input())
    second_set.add(second_num)

print(*first_set.intersection(second_set), sep="\n")

# n, m = [int(x) for x in input().split()]
#
# first_set = {input() for _ in range(n)}
# second_set = {input() for _ in range(m)}
#
# print(*first_set.intersection(second_set), sep="\n")