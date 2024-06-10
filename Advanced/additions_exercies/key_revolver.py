from collections import deque

price_of_bullet = int(input())
size_of_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence = int(input())
copy_size_of_barrel = size_of_barrel
bullets_counter = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_lock >= current_bullet:
        print('Bang!')
    else:
        locks.appendleft(current_lock)
        print("Ping!")

    copy_size_of_barrel -= 1
    bullets_counter += 1

    if copy_size_of_barrel == 0 and len(bullets) > 0:
        copy_size_of_barrel = size_of_barrel
        print("Reloading!")

bullets_cost = bullets_counter * price_of_bullet
total = intelligence - bullets_cost

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${total}" )

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")