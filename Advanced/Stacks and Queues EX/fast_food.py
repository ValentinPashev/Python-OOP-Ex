# from collections import deque
#
# quantity_of_food = int(input())
# deck_with_food = deque([int(x) for x in input().split()])
#
#
# print(max(deck_with_food))
#
# for order in deck_with_food.copy():
#     if quantity_of_food >= order:
#         deck_with_food.popleft()
#         quantity_of_food -= order
#
#     else:
#         print(f'Orders left:', *deck_with_food)
#         break
#
# else:
#     print(f'Orders complete')

from collections import deque

quantity_of_food = int(input())

deck_with_food = deque(int(x) for x in input().split())

copy_of_deck_of_food = deck_with_food.copy()

print(max(deck_with_food))

for order in deck_with_food:
    current_order = copy_of_deck_of_food.popleft()
    if quantity_of_food >= current_order:
        quantity_of_food -= current_order

    else:
        copy_of_deck_of_food.appendleft(current_order)
        break

if copy_of_deck_of_food:
    print(f'Orders left:', *copy_of_deck_of_food)

else:
    print(f'Orders complete')
