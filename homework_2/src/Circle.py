from homework_2.src.Figure import Figure
from math import pi


class Circle(Figure):
    name = "Circle"

    def __init__(self, diametr):
        if type(diametr) not in [int, float]:
            raise ValueError("Передано не числовое значение!")
        self.diametr = diametr

    @property
    def area(self):
        return pi * (self.diametr ** 2) / 4

    @property
    def perimetr(self):
        return pi * self.diametr

