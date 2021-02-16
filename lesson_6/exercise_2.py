"""
2) Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    def __init__(self, _length, _width, _specific_asphalt_mass, _asphalt_thickness):
        self._length = _length
        self._width = _width
        self._specific_asphalt_mass = _specific_asphalt_mass
        self._asphalt_thickness = _asphalt_thickness

    def mass_calc(self):
        asphalt_mass = self._length * self._width * self._specific_asphalt_mass * self._asphalt_thickness
        return f"Масса асфальта дороги дилнной {self._length} м, шириной {self._width} м, удельной массы" \
               f" {self._specific_asphalt_mass} кг/кв. м и толщиной {self._asphalt_thickness} м составляет: " \
               f"{asphalt_mass} кг"


m1 = Road(5000, 20, 25, 0.05)
print(m1.mass_calc())
