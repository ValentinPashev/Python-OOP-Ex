
try:
    text = input()
    times = int(input())

    result = ''

    for i in range(times):
        result += text
    print(result)

except ValueError:
    print(f"Variable times must be an integer")
