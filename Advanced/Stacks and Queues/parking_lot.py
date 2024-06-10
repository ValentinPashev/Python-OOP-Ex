# number = int(input())
#
# parking_lot = set()
#
# for car_numbers in range(number):
#     direction, reg_number = input().split(', ')
#
#     if direction == "IN":
#         parking_lot.add(reg_number)
#
#     elif direction == "OUT":
#         parking_lot.remove(reg_number)
#
# if parking_lot:
#     for item in parking_lot:
#         print(item)
#
# else:
#     print(f'Parking Lot is Empty')




number_of_cars = int(input())

parking_garage = set()

for cars in range(number_of_cars):
    direction, car_number = input().split(", ")

    if direction == "IN":
        parking_garage.add(car_number)

    elif direction == "OUT":
        parking_garage.remove(car_number)


if parking_garage:
    for car in parking_garage:
        print(car)


else:
    print(f'Parking Lot is Empty')




















