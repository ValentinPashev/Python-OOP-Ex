from collections import deque

command = input()

paid_clients = deque()


while command != "End":

    if command != "Paid":
        paid_clients.append(command)

    if command == "Paid":
        for item in range(len(paid_clients)):
            print(paid_clients.popleft())

    command = input()

print(f"{len(paid_clients)} people remaining.")