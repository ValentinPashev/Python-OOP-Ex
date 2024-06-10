numbers_list = [int(x) for x in input().split(", ")]

result = 1

for item in numbers_list:

    number = item
    if number <= 5:
        result *= number

    elif 5 < number <= 10:
        result /= number


print(float(result))