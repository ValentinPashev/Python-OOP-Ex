# This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import time

print("begin timer")
measure1 = time.time()
measure2 = time.time()

count = 1

while count < 11:
    if measure2 - measure1 >= 2:
        print("two seconds")
        measure1 = measure2
        measure2 = time.time()
        count += 1
    else:
        measure2 = time.time()

print("done")