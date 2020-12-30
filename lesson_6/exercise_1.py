"""
1) Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep
from sys import exit


class TrafficLight:
    def __init__(self, traffic_light_number, first_color, second_color, third_color):
        self.first_color = first_color
        self.second_color = second_color
        self.third_colow = third_color
        self.traffic_light_number = traffic_light_number
        print(f"Проверка работы светофора № {self.traffic_light_number}")

    # colors = ["Красный", "Жёлтый", "Зелёный"]

    def running(self):
        colors = [self.first_color, self.second_color, self.third_colow]
        if colors != ["Красный", "Жёлтый", "Зелёный"]:
            print("Неверный порядок режимов работы светофора")
            exit()
        for color in colors:
            print(f"Цвет светофора: {color}")
            if color == "Красный":
                sleep(7)
            elif color == "Жёлтый":
                sleep(2)
            elif color == "Зелёный":
                sleep(3)


t1 = TrafficLight(1, "Красный", "Жёлтый", "Зелёный")
t1.running()
t2 = TrafficLight(2, "Жёлтый", "Красный", "Зелёный")
t2.running()
