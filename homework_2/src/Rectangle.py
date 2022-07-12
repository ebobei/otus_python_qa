from homework_2.src.Figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, side_a, side_b):
        for item in [side_a, side_b]:
            if type(item) not in [int, float]:
                raise ValueError("Передано не числовое значение!")

        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimetr(self):
        return (self.side_a + self.side_b) * 2

