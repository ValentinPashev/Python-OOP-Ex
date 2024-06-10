from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())


toys = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()

    total_magic_level = current_material * current_magic

    if current_material == 0 or current_magic == 0:
        if current_material == 0:
            magic_levels.appendleft(current_magic)
        if current_magic == 0:
            materials.append(current_material)
        continue

    if total_magic_level < 0:
        materials_to_add = current_material + current_magic
        materials.append(materials_to_add)

    if total_magic_level == 150:
        toys['Doll'] += 1

    elif total_magic_level == 250:
        toys['Wooden train'] += 1

    elif total_magic_level == 300:
        toys['Teddy bear'] += 1

    elif total_magic_level == 400:
        toys['Bicycle'] += 1

    else:
        if total_magic_level > 0:
            materials.append(current_material + 15)

if toys['Doll'] > 0 and toys["Wooden train"] > 0:
    print("The presents are crafted! Merry Christmas!")

elif toys['Teddy bear'] > 0 and toys["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")


if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for key, value in toys.items():
    if value == 0:
        continue
    else:
        [print(f"{key}: {value}") for toy in sorted(set(toys))]
