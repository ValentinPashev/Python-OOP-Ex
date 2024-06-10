from collections import deque

money = [int(x) for x in input().split()]
snack_prices = deque(int(x) for x in input().split())
foods = 0

while money and snack_prices:
    current_money = money.pop()
    current_snack_price = snack_prices.popleft()

    if current_money == current_snack_price:
        foods += 1

    elif current_money > current_snack_price:
        foods += 1
        change = current_money - current_snack_price
        if money:
            money[-1] += change

    elif current_money < current_snack_price:
        continue

if foods == 0:
    print("Henry remained hungry. He will try next weekend again.")

elif foods >= 4:
    print(f"Gluttony of the day! Henry ate {foods} foods.")

else:
    if foods == 1:
        print(f"Henry ate: {foods} food.")
    else:
        print(f"Henry ate: {foods} foods.")

