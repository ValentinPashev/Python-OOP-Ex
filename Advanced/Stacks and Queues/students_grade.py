# number_of_students = int(input())
#
# students = {}
#
#
# for student in range(number_of_students):
#     name, grade = input().split()
#     if name not in students:
#         students[name] = []
#     students[name].append(float(grade))
#
# for student_name, grades in students.items():
#     formatted_grades = ' '.join([f"{grade:.2f}" for grade in grades])
#     print(f"{student_name} -> {formatted_grades} (avg: {sum(grades)/len(grades):.2f})")





number_of_students = int(input())

dict_of_students = {}

for student_info in range(number_of_students):
    name, grade = input().split()

    if name not in dict_of_students:
        dict_of_students[name] = []

    dict_of_students[name].append(float(grade))

for key, value in dict_of_students.items():
    average_grade = sum(value) / len(value)
    formatted_grades = ' '.join([f"{grade:.2f}" for grade in value])
    print(f"{key} -> {formatted_grades} (avg: {average_grade:.2f})")




















