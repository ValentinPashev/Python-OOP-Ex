names = int(input())
set_with_names = set()


for name in range(names):
    new_name = input()
    set_with_names.add(new_name)

print(*set_with_names, sep="\n")