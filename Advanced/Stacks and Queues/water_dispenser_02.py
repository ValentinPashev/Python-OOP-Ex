from collections import deque

quantity = int(input())

name = input()
name_list = deque()


while name != "Start":
    name_list.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()

    if len(data) == 1:
        liter_to_give = int(data[0])
        person_name = name_list.popleft()
        if liter_to_give <= quantity:
            print(f"{person_name} got water")
            quantity -= liter_to_give



        else:
            print(f"{person_name} must wait")

    else:
        liters_to_fill = int(data[1])
        quantity += liters_to_fill

    command = input()

print(f"{quantity} liters left")