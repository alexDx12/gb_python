"""
2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
"""


class Clothes:
    def __init__(self, coat_size, suit_growth):
        self.coat_size = coat_size
        self.suit_growth = suit_growth

    @property
    def square(self):
        square_calc = round(self.coat_size / 6.5 + 0.5 + 2 * self.suit_growth + 0.3)
        return f"Расход ткани на весь набор одежды составляет {square_calc} м2"
        #  можно ли дописывать сюда свойства дальше? Как идентифицируются границы блока?

class Coat(Clothes):
    def __init__(self, coat_size):
        self.coat_size = coat_size

    @property
    def square(self):
        square_calc = round(self.coat_size / 6.5 + 0.5)
        return f"Расход ткани на пальто составляет {square_calc} м2"


class Suit(Clothes):
    def __init__(self, suit_growth):
        self.suit_growth = suit_growth

    @property
    def square(self):
        square_calc = round(2 * self.suit_growth + 0.3)
        return f"Расход ткани на костюм составляет {square_calc} м2"


clothes_set = Clothes(1, 2)
print(clothes_set.square)
my_coat = Coat(1)
print(my_coat.square)
my_suit = Suit(2)
print(my_suit.square)
