"""
2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class CustomException(Exception):
    def __init__(self):
        self.txt = "На ноль делить нельзя, т.к. результат будет равен бесконечности."

    def division(self, divided, divisor):
        try:
            quotient = divided / divisor
        except ZeroDivisionError:
            print(self.txt)
        else:
            print(f'Результат деления {divided} на {divisor} равен {quotient}.')
        finally:
            print('Программа завершена.')


CustomException().division(5, 0)
CustomException().division(5, 2)
