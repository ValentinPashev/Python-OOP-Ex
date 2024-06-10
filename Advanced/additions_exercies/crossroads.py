from collections import deque

textile = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

patch = 30
bandage = 40
medkit = 100

dict_with_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textile and medicaments:
    current_textile = textile.popleft()
    current_medicine = medicaments.pop()

    if current_medicine + current_textile == 30:
        dict_with_items["Patch"] += 1

    elif current_medicine + current_textile == 40:
        dict_with_items["Bandage"] += 1

    elif current_medicine + current_textile == 100:
        dict_with_items["MedKit"] += 1

    elif current_medicine + current_textile > 100:
        dict_with_items["MedKit"] += 1
        additional_sum = (current_medicine + current_textile) - 100
        element_for_additional_sum = medicaments.pop() + additional_sum
        medicaments.append(element_for_additional_sum)

    else:
        current_medicine += 10
        medicaments.append(current_medicine)

if not textile and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textile:
    print("Textiles are empty.")

elif not medicaments:
    print("Medicaments are empty.")

sorted_dict = sorted(dict_with_items.items(), key=lambda x: (-(x[1]), x[0]))

for key, value in sorted_dict:
    if value == 0:
        continue
    else:
        print(f"{key} - {value}", end="\n")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")

if textile:
    print(f"Textiles left: {', '.join(str(x) for x in textile)}")
