from collections import deque


def fill_the_box(high, length, width, *args):
    size_of_grand_cube = high * length * width
    list_with_cubes = deque()
    for x in args:
        if x == "Finish":
            break
        else:
            list_with_cubes.append(int(x))

    while size_of_grand_cube > 0 and list_with_cubes:
        cube = list_with_cubes.popleft()
        if size_of_grand_cube > cube:
            size_of_grand_cube -= cube

        else:
            cube_to_be_added = abs(size_of_grand_cube - cube)
            list_with_cubes.append(cube_to_be_added)

            return f"No more free space! You have {sum(list_with_cubes)} more cubes."

    if size_of_grand_cube > 0:
        return f"There is free space in the box. You could put {size_of_grand_cube} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

