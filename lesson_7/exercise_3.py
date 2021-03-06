"""
3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()) ,
умножение (__mul__()) , деление (__truediv__()). Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n*****.
"""


# !!! Первый пример не соотвествует вышеприведённому условияю "Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся". Упражнение выполнено в соотвествии с приведённым примером в
# описании задачи.

class Cell:
    def __init__(self, number_of_elements):
        self.number_of_elements = int(number_of_elements)

    def __add__(self, other):
        return f'Результат сложения клеток: {self.number_of_elements + other.number_of_elements}'

    def __sub__(self, other):
        difference = self.number_of_elements - other.number_of_elements
        return f'Реузультат вычитания клеток: {difference if difference > 0 else "ошибка вычитания (количество ячеек должно быть больше 0)"}'

    def __mul__(self, other):
        return f'Результат умножения клеток: {self.number_of_elements * other.number_of_elements}'

    def __truediv__(self, other):
        return f'Результат деления клеток: {self.number_of_elements // other.number_of_elements}'

    def make_order(self, elements_in_row):
        result = ''
        number_of_full_rows = self.number_of_elements // elements_in_row
        number_of_residual_elements = self.number_of_elements - number_of_full_rows * elements_in_row
        for i in range(number_of_full_rows):
            result += f'{"*" * elements_in_row}\n'
        result += f'{"*" * number_of_residual_elements}'
        return f'Результат упорядочивания клетки:\n{result}'


first_cell = Cell(239)
second_cell = Cell(25)
print(first_cell + second_cell)
print(first_cell - second_cell)
print(second_cell - first_cell)
print(first_cell * second_cell)
print(first_cell / second_cell)
print(first_cell.make_order(50))
print(second_cell.make_order(5))
