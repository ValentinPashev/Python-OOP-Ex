number_of_names = int(input())

set_with_names = set()

for _ in range(number_of_names):
    name = input()
    set_with_names.add(name)

for n in set_with_names:
    print(n)