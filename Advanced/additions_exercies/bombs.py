from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = [int(x) for x in input().split(", ")]

dict_bombs = {"Datura Bombs": 0,
              "Cherry Bombs": 0,
              "Smoke Decoy Bombs": 0}

dict_values = {40 : "Datura Bombs",
               60 : "Cherry Bombs",
               120 : "Smoke Decoy Bombs"}


while bomb_casings and bomb_effects:
    if dict_bombs["Datura Bombs"] >= 3 and dict_bombs["Cherry Bombs"] >= 3 and dict_bombs["Smoke Decoy Bombs"] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break

    bomb_eff = bomb_effects.popleft()
    bomb_cas = bomb_casings.pop()
    total = bomb_eff + bomb_cas

    if total in dict_values.keys():
        key_for_bomb = dict_values[total]
        dict_bombs[key_for_bomb] += 1

    else:
        bomb_cas -= 5
        bomb_casings.append(bomb_cas)
        bomb_effects.appendleft(bomb_eff)


else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")

else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")

else:
    print("Bomb Casings: empty")

for key, value in sorted(dict_bombs.items()):
    print(f"{key}: {value}")



