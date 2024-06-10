def cookbook(*recipes):
    cuisine_recipes_dict = {

    }

    cuisine_number = {

    }

    for data in recipes:

        dish = data[0]
        cuisine = data[1]
        ingredients = data[2]

        if cuisine not in cuisine_recipes_dict:
            cuisine_recipes_dict[cuisine] = []
            cuisine_number[cuisine] = 0

        cuisine_recipes_dict[cuisine].append((dish, ingredients))
        cuisine_number[cuisine] += 1

    sorted_cuisines_dict = sorted(cuisine_number.keys(), key=lambda x: (-cuisine_number[x], x))

    cookbible = ""

    for cooking_info in sorted_cuisines_dict:
        cookbible += f"{cooking_info} cuisine contains {cuisine_number[cooking_info]} recipes:\n"
        sorted_recipes = sorted(cuisine_recipes_dict[cooking_info], key=lambda x: x[0])

        for recipe in sorted_recipes:

            recipe_name = recipe[0]
            ingredients = recipe[1]

            cookbible += f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}\n"

    return cookbible


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))