def age_assignment(*args, **name_data):
    result = []
    for letter, age in name_data.items():
        for name in args:
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")
                break

    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
