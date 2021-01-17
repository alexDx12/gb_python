"""
7) Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата.
"""


class ComlexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'z = {self.a} + {self.b}*i'

    def __add__(self, other):
        return ComlexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComlexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


z1 = ComlexNumber(2, 3)
z2 = ComlexNumber(-1, 1)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)