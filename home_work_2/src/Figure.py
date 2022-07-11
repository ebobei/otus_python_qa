class Figure:

    def __init__(self):
        raise ValueError("Геометрическую фигуру создать нельзя!")

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError("Передана не геометрическая фигура!")