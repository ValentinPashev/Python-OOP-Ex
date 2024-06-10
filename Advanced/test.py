#
# info = input().split(">>")
#
# revenue_collected = 0
#
# for i in range(len(info)):
#     data = info[i]
#     details = data.split()
#     car_type = details[0]
#     years = int(details[1])
#     kilometers = int(details[2])
#
#     total_tax = 0
#     initial_tax = 0
#     x = 0
#
#     if car_type == "family":
#         initial_tax = 50
#         x = (kilometers // 3000)
#         total_tax = x * 12 + (initial_tax - years * 5)
#         revenue_collected += total_tax
#
#     elif car_type == "heavyDuty":
#         initial_tax = 80
#         x = (kilometers // 9000)
#         total_tax = x * 14 + (initial_tax - years * 8)
#         revenue_collected += total_tax
#
#     elif car_type == "sports":
#         initial_tax = 100
#         x = (kilometers // 2000)
#         total_tax = x * 18 + (initial_tax - years * 9)
#         revenue_collected += total_tax
#
#     else:
#         print("Invalid car type")
#         continue
#
#     print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")
#
# print(f"The National Revenue Agency will collect {revenue_collected:.2f} euros in taxes.")
#
#
#
# #
# #
# #
# #
# #
# my_dict = {'key1': [1, 2, 3], 'key2': [4, 5, 6], 'key3': [7, 8, 9]}
#
# # Unpack lists using a loop
# unpacked_values = []
# for key, value_list in my_dict.items():
#     unpacked_values.extend(value_list)
#
# # Alternatively, you can use a list comprehension
# # unpacked_values = [value for value_list in my_dict.values() for value in value_list]
#
# print(unpacked_values)

#
# n = 5  # Replace 5 with the desired value of n
# message = "Reached altitudes: "
# for altitude in range(1, n + 1):
#     message += f"Altitude {altitude}, "
# print(message[:-2])  # Removing the trailing comma and space

#
# from collections import deque
#
# initial_fuel = [int(x) for x in input().split()]
# additional_index = deque(int(x) for x in input().split())
# necessary_fuel = deque(int(x) for x in input().split())
# altitude = 0
# result = 'Reached altitudes: '
# copy_of_necessary_fuel = len(necessary_fuel)
#
# while initial_fuel and necessary_fuel:
#     current_fuel = initial_fuel.pop()
#     additional_consumption = additional_index.popleft()
#     current_necessary_fuel = necessary_fuel.popleft()
#     total_fuel = current_fuel - additional_consumption
#
#     if total_fuel >= current_necessary_fuel:
#         altitude += 1
#         print(f"John has reached: Altitude {altitude}")
#
#     elif total_fuel < current_necessary_fuel: #and altitude > 0
#         print(f"John did not reach: Altitude {altitude + 1}")
#         if altitude > 0:
#             print('John failed to reach the top.')
#             for al in range(1, altitude + 1):
#                 result += f"Altitude {al}, "
#             print(result[:-2])
#         break
#
#     elif total_fuel < current_necessary_fuel and altitude == 0:
#         print("John failed to reach the top.")
#         print("John didn't reach any altitude.")
#
# if altitude == copy_of_necessary_fuel:
#     print(f"John has reached all the altitudes and managed to reach the top!")
#
#
# def softuni_students(*args, **kwargs):
#     invalid_students = []
#     a = 5
#     linked_students = {}
#     for id, name in args:
#         course_id = id
#         if course_id in kwargs.keys():
#             linked_students[name] = course_id
#
#     sorted_dict_with_users = dict(sorted(linked_students.items(), key= lambda x: x))
#
#     for student, course in sorted_dict_with_users.items():
#         print(f"*** A student with the username {student} has successfully finished the course {linked_students[student]}!")
#
#     for item in invalid_students:
#         print(f"!!! Invalid course students: {item}")
#
#
#
# print(softuni_students(
#     ('id_22', 'Programmingkitten'),
#     ('id_11', 'MitkoTheDark'),
#     ('id_321', 'Bobosa253'),
#     ('id_08', 'KrasimirAtanasov'),
#     ('id_32', 'DaniBG'),
#     id_321='HTML & CSS',
#     id_22='Machine Learning',
#     id_08='JS Advanced',
# ))