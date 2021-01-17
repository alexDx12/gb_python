"""
1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""


class Data:
    def __init__(self, data_string):
        self.data_string = data_string

    @classmethod
    def data_execution(cls, data_string):
        data_list = data_string.split('-')
        new_list = [int(i) for i in data_list]
        print(f'Число: {new_list[0]}\nМесяц: {new_list[1]}\nГод: {new_list[2]}')

    @staticmethod
    def data_validation(data_string):
        data_list = data_string.split('-')
        new_list = [int(i) for i in data_list]
        if new_list[0] < 1 or new_list[0] > 31:
            print('День введён некорректно.')
        if new_list[1] < 1 or new_list[1] > 12:
            print('Месяц введён некорректно.')
        if new_list[2] < 2000 or new_list[1] > 2021:
            print('Год введён некорректно.')


data_1 = '06-04-2005'
data_2 = '00-00-1900'
Data.data_execution(data_1)
Data.data_validation(data_1)
Data.data_execution(data_2)
Data.data_validation(data_2)
