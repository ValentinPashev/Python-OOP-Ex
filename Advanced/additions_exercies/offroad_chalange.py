from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_index = deque(int(x) for x in input().split())
necessary_fuel = deque(int(x) for x in input().split())
altitude = 0
result = 'Reached altitudes: '
copy_of_necessary_fuel = len(necessary_fuel)

while initial_fuel and necessary_fuel:
    current_fuel = initial_fuel.pop()
    additional_consumption = additional_index.popleft()
    current_necessary_fuel = necessary_fuel.popleft()
    total_fuel = current_fuel - additional_consumption

    if total_fuel >= current_necessary_fuel:
        altitude += 1
        print(f"John has reached: Altitude {altitude}")

    elif total_fuel < current_necessary_fuel: #and altitude > 0
        print(f"John did not reach: Altitude {altitude + 1}")
        if altitude > 0:
            print('John failed to reach the top.')
            for al in range(1, altitude + 1):
                result += f"Altitude {al}, "
            print(result[:-2])

        elif total_fuel < current_necessary_fuel and altitude == 0:
            print("John failed to reach the top.")
            print("John didn't reach any altitude.")
        break
if altitude == copy_of_necessary_fuel:
    print(f"John has reached all the altitudes and managed to reach the top!")


