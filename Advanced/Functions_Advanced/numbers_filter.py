def even_odd_filter(**dict_of_numbers):
    if "odd" in dict_of_numbers:
        dict_of_numbers["odd"] = [n for n in dict_of_numbers["odd"] if n % 2 != 0]

    if "even" in dict_of_numbers:
        dict_of_numbers["even"] = [n for n in dict_of_numbers["even"] if n % 2 == 0]

    return dict(sorted(dict_of_numbers.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))