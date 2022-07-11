from homework_2.src.Figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, side):
        if type(side) not in [int, float]:
            raise ValueError("Передано не числовое значение!")
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimetr(self):
        return self.side * 4
