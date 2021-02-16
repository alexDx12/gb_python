"""
5) Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.
"""

with open('exercise_5.txt', 'w', encoding='utf-8') as file:
    user_string = input("Введите строку целых числел, разделённых пробелами: ")
    file.write(user_string)

with open('exercise_5.txt', 'r', encoding='utf-8') as file:
    user_list = file.readline().split(' ')
    user_numbers = [int(number) for number in user_list]

print(f'Сумма введёных элементов: {sum(user_numbers)}')