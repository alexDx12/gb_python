"""
4) Реализуйте базовый класс Car .
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police:
            print("Внимание! Полиция! Уступите дорогу!")

    def go(self):
        print(f"Автомобиль {self.name} едет")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self):
        print(f"Автомобиль {self.name} повернул")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name}: {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name}: {self.speed}*")  # * для контроля переопределения метода
        if self.speed > 60:
            print("Внимание! Превышение скорости!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name}: {self.speed}**")  # ** для контроля переопределения метода
        if self.speed > 40:
            print("Внимание! Превышение скорости!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = TownCar(50, "red", "Audi A5", False)
audi.go()
audi.stop()
audi.turn()
audi.show_speed()

suzuki = TownCar(90, "blue", "Suzuki Vitara", False)
suzuki.go()
suzuki.stop()
suzuki.turn()
suzuki.show_speed()

mercedes = SportCar(200, "Silver", "Mercedes F1", False)
mercedes.go()
mercedes.stop()
mercedes.turn()
mercedes.show_speed()

peugeot = WorkCar(30, "Black", "Peugeot Traveller", False)
peugeot.go()
peugeot.stop()
peugeot.turn()
peugeot.show_speed()

gazelle = WorkCar(60, "White", "Gazelle Next", False)
gazelle.go()
gazelle.stop()
gazelle.turn()
gazelle.show_speed()

ford = PoliceCar(100, "White", "Ford Focus", True)
ford.go()
ford.stop()
ford.turn()
ford.show_speed()