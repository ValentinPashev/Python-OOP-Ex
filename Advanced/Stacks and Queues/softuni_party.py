guests = int(input())

set_of_guests = set()

for client in range(guests):
    guest = input()
    set_of_guests.add(guest)


command = input()

while command != "END":
    if command in set_of_guests:
        set_of_guests.remove(command)

    command = input()

print(len(set_of_guests))
for customer in sorted(set_of_guests):
    print(customer)