"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""

file = open('exercise_2.txt', 'w', encoding='utf-8')
user_strings = []
while True:
    user_string = input('Введите строку или нажмите enter: ')
    if user_string == "":
        break
    else:
        user_strings.append(user_string + '\n')
file.writelines(user_strings)

with open('exercise_2.txt', 'r') as file:
    string_number = 0
    for string in file:
        string_number += 1
        words = string.split(' ')
        print(f'Строка №{string_number} "{string}", количество слов: {len(words)}')
    print(f'Общее количество строк: {string_number}')
