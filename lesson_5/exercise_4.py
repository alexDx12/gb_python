"""
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""

rus_numbers = ['Один', 'Два', 'Три', 'Четыре']
rus_strings = []
with open('exercise_4.txt', 'r', encoding='utf-8') as file:
    count = 0
    for eng_string in file:
        elements = eng_string.split()
        rus_strings.append(f'{rus_numbers[count]} {elements[1]} {elements[2]} \n')
        count += 1
with open('exercise_4_new.txt', 'w', encoding='utf-8') as file:
    file.writelines(rus_strings)

