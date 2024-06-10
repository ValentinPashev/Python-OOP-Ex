number_of_elements = int(input())
my_set = set()

for _ in range(number_of_elements):
    current_els = input().split()

    for el in current_els:
        my_set.add(el)


print(*my_set, sep="\n")

# print(*{el for _ in range(int(input())) for el in input().split()}, sep="\n")
# not a good idea