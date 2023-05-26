# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names_of_students = []
for student in students:
    if student not in names_of_students:
        names_of_students.append(student)
for student in names_of_students:
    print(f'{student["first_name"]}: {students.count(student)}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

print(
    f'Самое популярное имя среди учеников - '
    f'{max(students, key=students.count)["first_name"]}'
    )

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for school_class, name in enumerate(school_students):
    print(
        f'Самое популярное имя в классе {school_class + 1}: '
        f'{max(name, key=name.count)["first_name"]}'
        )

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for school_class in school:
    boys = []
    girls = []
    for student in school_class['students']:
        if is_male[student['first_name']] is True:
            boys.append(student['first_name'])
        elif is_male[student['first_name']] is False:
            girls.append(student['first_name'])
    print(
        f'Класс {school_class["class"]}: '
        f'девочки {len(girls)}, '
        f'мальчики {len(boys)}'
        )

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '4b', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Маша'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

boys_count_dict = {}
girls_count_dict = {}
for school_class in school:
    boys = []
    girls = []
    for student in school_class['students']:
        if is_male.get(student['first_name']) is True:
            boys.append(student['first_name'])
        elif is_male.get(student['first_name']) is False:
            girls.append(student['first_name'])
    boys_count_dict.update({len(boys): school_class["class"]})
    girls_count_dict.update({len(girls): school_class["class"]})
for count_girls, class_name in girls_count_dict.items():
    if count_girls is max(girls_count_dict.keys()):
        print(f'Больше всего девочек в классе {class_name}')
for count_boys, class_name in boys_count_dict.items():
    if count_boys is max(boys_count_dict.keys()):
        print(f'Больше всего мальчиков в классе {class_name}')
