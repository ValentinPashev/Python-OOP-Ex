from collections import deque


def list_manipulator(list_with_intigers, first_command, second_command, *args):
    deck_with_nums = deque(int(x) for x in list_with_intigers)
    list_to_be_added = []
    if args:
        if first_command == "add" and second_command == "beginning":
            for num in args:
                list_to_be_added.append(num)

            for x in range(len(list_to_be_added)):
                current_num = list_to_be_added.pop()
                deck_with_nums.appendleft(current_num)

        elif first_command == "add" and second_command == "end":
            for num in args:
                deck_with_nums.append(num)

        elif first_command == "remove" and second_command == "beginning":
            list_to_be_added.append(args)
            index = list_to_be_added[0]
            for _ in range(*index):
                deck_with_nums.popleft()

        elif first_command == "remove" and second_command == "end":
            list_to_be_added.append(args)
            index = list_to_be_added[0]
            for _ in range(*index):
                deck_with_nums.pop()

    else:
        if first_command == "remove" and second_command == "end":
            deck_with_nums.pop()

        else:
            deck_with_nums.popleft()

    return [int(x) for x in deck_with_nums]


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
