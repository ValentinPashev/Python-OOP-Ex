def shop_from_grocery_list(budget, list_with_products, *args):
    already_purchased = set()
    shopping_list = list(list_with_products)
    # if len(shopping_list) == 0:
    #     for product in args:
    #         already_purchased.add(product[0])
    #     return f"You did not buy all the products. Missing products: {', '.join(x for x in already_purchased)}."

    for item in args:
        product = item[0]
        price = float(item[1])
        if price > budget:
            return f"You did not buy all the products. Missing products: {', '.join(x for x in shopping_list)}."

        if product not in already_purchased and product in shopping_list:
            budget -= price
            already_purchased.add(product)
            shopping_list = [item for item in shopping_list if item != product]

    if len(shopping_list) == 0:
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'
    else:
        return f"You did not buy all the products. Missing products: {', '.join(x for x in shopping_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "cola", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22))
)

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))

# print(shop_from_grocery_list(
#     100,
#     [],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))
