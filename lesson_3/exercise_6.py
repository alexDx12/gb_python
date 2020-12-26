"""
6) Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) ->
Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
использовать написанную ранее функцию int_func() .
"""


def int_func(word):
    result = word.title()
    return result


def new_func(words):
    word_list = words.split()
    result_list = []
    for word in word_list:
        result_list.append(int_func(word))
    result = " ".join(result_list)
    return result


print(int_func("text"))
print(new_func("hello world"))
