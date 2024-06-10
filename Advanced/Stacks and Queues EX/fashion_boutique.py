clothes_as_int = [int(x) for x in input().split()]
capacity_of_rack = int(input())

current_capacity = capacity_of_rack
racks_used = 1

while clothes_as_int:
    current_cloth = clothes_as_int.pop()
    if current_capacity >= current_cloth:
        current_capacity -= current_cloth
    else:
        racks_used += 1
        current_capacity = capacity_of_rack - current_cloth

print(racks_used)
