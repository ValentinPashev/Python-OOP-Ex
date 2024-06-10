from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches = 0

while males and females:
    current_male = males.pop()
    current_female = females.popleft()
    IS_CURRENT_MALE_ZERO = False
    IS_CURRENT_FEMALE_ZERO = False

    if current_female <= 0:
        IS_CURRENT_FEMALE_ZERO = True

    if current_male <= 0:
        IS_CURRENT_MALE_ZERO = True

    if IS_CURRENT_FEMALE_ZERO and IS_CURRENT_MALE_ZERO:
        continue

    elif IS_CURRENT_FEMALE_ZERO and IS_CURRENT_MALE_ZERO == False:
        males.append(current_male)
        continue

    elif IS_CURRENT_MALE_ZERO and IS_CURRENT_FEMALE_ZERO == False:
        females.appendleft(current_female)
        continue

    if current_male % 25 == 0 or current_female % 25 == 0:
        if current_male % 25 == 0:
            females.appendleft(current_female)
            if males:
                male_to_be_removed = males.pop()

        if current_female % 25 == 0:
            males.append(current_male)
            if females:
                female_to_be_removed = females.popleft()

        continue

    if current_female == current_male:
        matches += 1

    else:
        current_male -= 2
        males.append(current_male)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(str(x) for x in males[::-1])}")

else:
    print(f"Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")

else:
    print("Females left: none")