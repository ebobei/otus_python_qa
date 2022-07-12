import math
from homework_2.src.Figure import Figure


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, side_a, side_b, side_c):
        for item in [side_a, side_b, side_c]:
            if type(item) not in [int, float]:
                raise ValueError("Передано не числовое значение!")

        max_side = max(side_a, side_b, side_c)
        if max_side < (side_a + side_b + side_c) - max_side:
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            raise ValueError("Геометрическую фигуру создать нельзя!")

    @property
    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    @property
    def perimetr(self):
        return self.side_a + self.side_b + self.side_c

