def softuni_students(*args, **kwargs):
    valid_students = {}
    invalid_students = set()
    for data in args:
        course_id = data[0]
        username = data[1]

        if course_id in kwargs.keys():
            valid_students[username] = kwargs[course_id]
        else:
            invalid_students.add(username)

    sorted_dict = sorted(valid_students.items())
    result = []

    for student, course in sorted_dict:
        result.append(f"*** A student with the username {student} has successfully finished the course {course}!")

    if invalid_students:
        invalid_message = f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
        result.append(invalid_message)

    return '\n'.join(result)


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))