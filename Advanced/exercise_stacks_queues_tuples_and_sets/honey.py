from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
sequence_of_symbols = deque(input().split())

total_honey_made = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    if current_bee > current_nectar:
        bees.appendleft(current_bee)

    else:
        current_symbol = sequence_of_symbols.popleft()

        if current_symbol == "+":
            total_honey_made += current_bee + current_nectar

        elif current_symbol == "-":
            honey_produced = abs(current_bee - current_nectar)
            total_honey_made += honey_produced

        elif current_symbol == "*":
            total_honey_made += current_bee * current_nectar

        elif current_symbol == "/":
            if current_nectar == 0:
                continue
            else:
                total_honey_made += current_bee / current_nectar

print(f"Total honey made: {total_honey_made}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")