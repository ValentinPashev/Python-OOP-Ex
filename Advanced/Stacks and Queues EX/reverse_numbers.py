from collections import deque

numbers = deque(input().split())

for _ in range(len(numbers)):
    print(numbers.pop(), end=" ")

#
# numbers = [int(x) for x in input().split()]
# reversed_stack = []
#
# while numbers:
#     reversed_stack.append(numbers.pop())
#
# print(*reversed_stack)
