# numbers = tuple(float(number) for number in input().split())
#
# occ = {}
#
# for number in numbers:
#     occ[number] = numbers.count(number)
#
# for key, value in occ.items():
#     print(f"{key} - {value} times")

numbers = tuple(float(number) for number in input().split())

dict_of_number = {}

for n in numbers:
    dict_of_number[n] = numbers.count(n)


for key, value in dict_of_number.items():
    print(f"{key} - {value} times")