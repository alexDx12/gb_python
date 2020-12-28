"""
3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

from statistics import mean

file = open('exercise_3.txt', 'w', encoding='utf-8')
while True:
    employee = input('Введите имя сотрудника и его оклад через пробел или нажмите enter: ')
    if employee == "":
        break
    else:
        file.write(employee + '\n')

file = open('exercise_3.txt', 'r', encoding='utf-8')
underpaid_employees = []
salaries = []
for employee in file:
    salaries.append(int(employee.split()[1]))
    if int(int(employee.split()[1])) < 20000:
        underpaid_employees.append(employee.split()[0])
print(f'Сотрудники с зарплатами ниже 20000: {underpaid_employees}, средняя зарплата сотрудников: {mean(salaries)}.')
