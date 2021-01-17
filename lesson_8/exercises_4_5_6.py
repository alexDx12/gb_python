"""
4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.

5) Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).

6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Stock:
    """Класс склад. Предназанчен для сбора оргтехники и её распределения между подразделениями компании."""

    def __init__(self, square, storage_type):
        """
        :param square: параметр, определяющий площадь склада, кв. м
        :param storage_type: параметр, определяющий тип склада (warm, cold)
        """
        self.square = square
        self.type = storage_type
        self.equipment = {}  # словарь, содержащий типы и количество оборудования, помещённого на склад
        self.department_A = {}  # словарь, содержащий типы и количество оборудования, отгруженного в отдел А
        self.department_B = {}  # словарь, содержащий типы и количество оборудования, отгруженного в отдел B
        self.department_C = {}  # словарь, содержащий типы и количество оборудования, отгруженного в отдел С

    def __str__(self):
        return f'Оборудование, хранимое на складе:\n{self.equipment}\n' \
               f'Оборудование, отгруженное в отдел А:\n{self.department_A}\n' \
               f'Оборудование, отгруженное в отдел B:\n{self.department_B}\n' \
               f'Оборудование, отгруженное в отдел C:\n{self.department_C}\n'

    def get_equipment(self, equipment, quantity):
        """
        Функция приёма оборудования на склад.
        :param equipment: тип оборудования, помещаемого на склад (Printer, Scanner, Copier)
        :param quantity: количество оборудования, помещаемого на склад, шт.
        :return: None
        """
        if equipment in self.equipment.keys():
            self.equipment[equipment] += quantity
        else:
            self.equipment[equipment] = quantity

    def pop_equipment(self, equipment, quantity, department):
        """
        Функция передачи оборудования в определённое подразделение компании.
        :param equipment: тип оборудования, отгружаемого со склада (Printer, Scanner, Copier)
        :param quantity: количество оборудования, отгружаемого со склада, шт.
        :param department: подразделение компании, в которое осуществляется отгрузка оборудования (A, B, C)
        :return: None или сообщение о количестве нехватающего оборудования для отгрузки в отдел компании
        """
        if self.equipment[equipment] >= quantity:
            self.equipment[equipment] -= quantity
            if department == 'A':
                actual_department = self.department_A
            elif department == 'B':
                actual_department = self.department_B
            elif department == 'C':
                actual_department = self.department_C
            if equipment in actual_department.keys():
                actual_department[equipment] += quantity
            else:
                actual_department[equipment] = quantity
        else:
            print(
                f'Не хватает {quantity - self.equipment[equipment]} единиц оборудования {equipment} для отгрузки в '
                f'отдел {department}.')


class Equipment:
    """Родительский класс для всего оборудования (оргтехники)."""

    def __init__(self, quantity, mass, year, cost):
        """
        :param quantity: параметр, определяющий количество оборудования, шт.
        :param mass: параметр, определяющий массу единицы оборудования, кг
        :param year: параметр, определяющий год выпуска оборудования
        :param cost: параметр, определяющий стоимость единицы оборудования, у.е.
        """
        self.quantity = quantity
        self.mass = mass
        self.year = year
        self.cost = cost


class Printer(Equipment):
    """Класс, описывающий принтеры."""

    def __init__(self, quantity, mass, year, cost, printer_type):
        """
        :param quantity: параметр, определяющий количество оборудования, шт.
        :param mass: параметр, определяющий массу единицы оборудования, кг
        :param year: параметр, определяющий год выпуска оборудования
        :param cost: параметр, определяющий стоимость единицы оборудования, у.е.
        :param printer_type: параметр, определяющий тип принтера (jet, laser)
        """
        super().__init__(quantity, mass, year, cost)
        self.equipment_type = 'Printer'
        self.printer_type = printer_type


class Scanner(Equipment):
    """Класс, описывающий сканеры."""

    def __init__(self, quantity, mass, year, cost, scanner_type):
        """
        :param quantity: параметр, определяющий количество оборудования, шт.
        :param mass: параметр, определяющий массу единицы оборудования, кг
        :param year: параметр, определяющий год выпуска оборудования
        :param cost: параметр, определяющий стоимость единицы оборудования, у.е.
        :param scanner_type: параметр, определяющий тип сканера (flatbed, stream)
        """
        super().__init__(quantity, mass, year, cost)
        self.equipment_type = 'Scanner'
        self.scanner_type = scanner_type


class Copier(Equipment):
    """Класс, описывающий ксероксы."""

    def __init__(self, quantity, mass, year, cost, copier_type):
        """
        :param quantity: параметр, определяющий количество оборудования, шт.
        :param mass: параметр, определяющий массу оборудования, кг
        :param year: параметр, определяющий год выпуска оборудования
        :param cost: параметр, определяющий стоимость оборудования, у.е.
        :param copier_type: параметр, определяющий тип ксерокса (black/white, color)
        """
        super().__init__(quantity, mass, year, cost)
        self.equipment_type = 'Copier'
        self.copier_type = copier_type


printer_set_1 = Printer(30, 8, 2015, 3000, 'jet')
printer_set_2 = Printer(20, 12, 2018, 4500, 'laser')
scanner_set_1 = Scanner(15, 3, 2019, 1500, 'flatbed')
copier_set_1 = Copier(18, 10, 2018, 2200, 'black/white')
my_stock = Stock(500, 'cold')
print(my_stock)
my_stock.get_equipment(printer_set_1.equipment_type, printer_set_1.quantity)
my_stock.get_equipment(printer_set_2.equipment_type, printer_set_2.quantity)
my_stock.get_equipment(scanner_set_1.equipment_type, scanner_set_1.quantity)
my_stock.get_equipment(copier_set_1.equipment_type, copier_set_1.quantity)
print(my_stock)
my_stock.pop_equipment('Printer', 35, 'A')
my_stock.pop_equipment('Printer', 1, 'A')
my_stock.pop_equipment('Scanner', 2, 'A')
my_stock.pop_equipment('Copier', 1, 'A')
my_stock.pop_equipment('Printer', 3, 'B')
my_stock.pop_equipment('Scanner', 4, 'B')
my_stock.pop_equipment('Copier', 6, 'B')
my_stock.pop_equipment('Printer', 3, 'C')
my_stock.pop_equipment('Scanner', 4, 'C')
my_stock.pop_equipment('Copier', 6, 'C')
print(my_stock)