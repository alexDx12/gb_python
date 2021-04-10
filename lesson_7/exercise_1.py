"""
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — с истема некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, list_of_rows):
        self.list_of_rows = list_of_rows

    def __str__(self):
        return "\n".join(str(row) for row in self.list_of_rows)

    def __add__(self, other):
        self.result = [[0 for column_index in range(len(self.list_of_rows[0]))]
                       for row_index in range(len(self.list_of_rows))]  # генерация нулевой матрицы
        for row_index in range(len(self.list_of_rows)):
            for column_index in range(len(self.list_of_rows[0])):
                self.result[row_index][column_index] = self.list_of_rows[row_index][column_index] + \
                                                       other.list_of_rows[row_index][column_index]
        return self.result


m1 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
m2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(m1 + m2)
print(m1)
print(m2)

# почему перегрузка __str__ не срабатывает на сумму матриц?