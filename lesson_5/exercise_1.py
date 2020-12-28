"""
1) Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

file = open('exercise_1.txt', 'w', encoding='utf-8')
user_strings = []
while True:
    user_string = input('Введите строку или нажмите enter: ')
    if user_string == "":
        break
    else:
        user_strings.append(user_string + '\n')
file.writelines(user_strings)
out = [word.strip() for word in user_strings]
file.close()
print(out)
