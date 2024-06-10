from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())
matches = 0
worms_counter = len(worms)

while len(holes) != 0 and len(worms) != 0:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm <= 0:
        continue

    if current_hole == current_worm:
        matches += 1
        worms_counter -= 1

    else:
        current_worm -= 3
        if current_worm <= 0:
            continue
        else:
            worms.append(current_worm)

if matches == 0:
    print('There are no matches.')

else:
    print(f"Matches: {matches}")

if len(worms) == 0 and worms_counter == 0:
    print(f"Every worm found a suitable hole!")

elif len(worms) == 0 and matches != 0:
    print("Worms left: none")

elif len(worms) == 0 and matches == 0:
    print("Worms left: none")

if worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if holes:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")

else:
    print("Holes left: none")
