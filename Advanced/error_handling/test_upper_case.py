password = input()

for char in password:
    if char.isdigit():
        print(f"Contains numbers")
        break
    else:
        print("Does not contain numbers")


