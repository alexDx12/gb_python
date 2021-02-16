"""
6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

with open('exercise_6.txt', 'r', encoding='utf-8') as file:
    result = {}
    for string in file:
        sub, lects, practs, labs = string.split()
        lects = lects.split('(л)')[0]
        if lects.isdigit():
            lects = int(lects)
        else:
            lects = 0
        practs = practs.split('(пр)')[0]
        if practs.isdigit():
            practs = int(practs)
        else:
            practs = 0
        labs = labs.split('(лаб)')[0]
        if labs.isdigit():
            labs = int(labs)
        else:
            labs = 0
        hours = lects + practs + labs
        result[sub] = hours
    print(result)
