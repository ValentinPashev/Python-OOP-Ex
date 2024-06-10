list = [1,2,3]

from collections import deque


def list_manipulator(list, *args):
    list_with_numbers = deque(int(x) for x in list)
    first_command = args[0]
    second_command = args[1]
    new_list = []
    if len(args) > 2:
        numbers = args[2:]

        if first_command == "add" and second_command == "beginning":
            for num in numbers:
                list_with_numbers.appendleft(num)

    return [int(x) for x in list_with_numbers]


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
