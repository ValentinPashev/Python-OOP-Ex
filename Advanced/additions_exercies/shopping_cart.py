def shopping_cart(*args):
    meals = {"Pizza": [], "Soup": [], "Dessert": []}
    last_product = ''
    max_soup = 3
    max_pizza = 4
    max_dessert = 2

    for meal_product in args:
        meal = meal_product[0]
        product = meal_product[1]

        if meal_product == "Stop":
            break

        if product in meals[meal]:
            continue

        elif meal == "Pizza" and max_pizza != 0:
            max_pizza -= 1
            meals[meal].append(product)

        elif meal == "Soup" and max_soup != 0:
            max_soup -= 1
            meals[meal].append(product)

        elif meal == "Dessert" and max_dessert != 0:
            max_dessert -= 1
            meals[meal].append(product)

        last_product = product

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), (x[0]), x[1]))

    for value in meals.values():
        if len(value) > 0:
            break
        else:
            return 'No products in the cart!'

    result = ''

    for tuple_ in sorted_meals:
        result += f"{tuple_[0]}:\n"
        sorted_product = sorted(tuple_[1])
        for product in sorted_product:
            result += f" - {product}\n"

    return result

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))