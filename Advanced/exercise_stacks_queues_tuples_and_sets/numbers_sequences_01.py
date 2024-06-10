first_sequences = set(int(x) for x in input().split())
second_sequences = set(int(y) for y in input().split())


for _ in range(int(input())):
    data = input().split()
    command = data[0] + " " + data[1]
    numbers = data[2:]

    if command == "Add First":
        for num in numbers:
            first_sequences.add(int(num))

    elif command == "Add Second":
        for num in numbers:
            second_sequences.add(int(num))

    elif command == "Remove First":
        for num in numbers:
            first_sequences.discard(int(num))

    elif command == "Remove Second":
        for num in numbers:
            second_sequences.discard(int(num))

    elif command == "Check Subset":
        print(first_sequences.issubset(second_sequences) or second_sequences.issubset(first_sequences))

print(*sorted(first_sequences), sep=", ")
print(*sorted(second_sequences), sep= ", ")