import pytest
from homework_2.src.Circle import Circle
from homework_2.src.Triangle import Triangle
from homework_2.src.Rectangle import Rectangle
from homework_2.src.Square import Square


def test_circle_name():
    circle = Circle(10)
    assert circle.name == "Circle"


def test_circle_negative_name():
    circle = Circle(10)
    assert circle.name != "Carcle"


circle_area = [
    (0, 0),
    (1, 0.7853981633974483),
    (5, 19.634954084936208)
]


@pytest.mark.parametrize("diametr, area", circle_area)
def test_circle_area_1(diametr, area):
    circle = Circle(diametr)
    assert circle.area == area


circle_perimetr = [
    (0, 0),
    (1, 3.141592653589793),
    (5, 15.707963267948966)
]


@pytest.mark.parametrize("diametr, perimetr", circle_perimetr)
def test_circle_area_2(diametr, perimetr):
    circle = Circle(diametr)
    assert circle.perimetr == perimetr


def test_circle_add_area():
    circle = Circle(5)
    square = Square(10)
    assert circle.add_area(square) == 119.634954084936208


def test_circle_add_negative_area():
    circle = Circle(5)
    square = Square(7)
    assert circle.add_area(square) != 119.634954084936208


def test_rectangle_name():
    rectangle = Rectangle(10, 5)
    assert rectangle.name == "Rectangle"


def test_rectangle_negative_name():
    rectangle = Rectangle(10, 5)
    assert rectangle.name != "Ractangle"


rectangle_area = [
    (0, 1, 0),
    (1, 2, 2)
]


@pytest.mark.parametrize("side_a, side_b, area", rectangle_area)
def test_rectangle_area_1(side_a, side_b, area):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.area == area


rectangle_perimetr = [
    (1, 2, 6),
    (5, 4, 18)
]


@pytest.mark.parametrize("side_a, side_b, perimetr", rectangle_perimetr)
def test_rectangle_area_2(side_a, side_b, perimetr):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.perimetr == perimetr


def test_rectangle_add_area():
    rectangle = Rectangle(10, 5)
    square = Square(5)
    assert rectangle.add_area(square) == 75


def test_rectangle_add_negative_area():
    rectangle = Rectangle(20, 5)
    square = Square(5)
    assert rectangle.add_area(square) != 75


def test_square_name():
    square = Square(10)
    assert square.name == "Square"


def test_square_negative_name():
    square = Square(10)
    assert square.name != "Ssuare"


square_area = [
    (0, 0),
    (1, 1),
    (5, 25)
]


@pytest.mark.parametrize("side, area", square_area)
def test_square_area_1(side, area):
    square = Square(side)
    assert square.area == area


square_perimetr = [
    (0, 0),
    (1, 4),
    (5, 20)
]


@pytest.mark.parametrize("side, perimetr", square_perimetr)
def test_square_area_1(side, perimetr):
    square = Square(side)
    assert square.perimetr == perimetr


def test_square_add_area_2():
    square_a = Square(10)
    square_b = Square(5)
    assert square_a.add_area(square_b) == 125


def test_square_add_negative_area_2():
    square_a = Square(40)
    square_b = Square(5)
    assert square_a.add_area(square_b) != 125


def test_triangle_name():
    triangle = Triangle(3, 4, 5)
    assert triangle.name == "Triangle"


def test_triangle_negative_name():
    triangle = Triangle(3, 4, 5)
    assert triangle.name != "Tsiangle"


triangle_area = [
    (1, 1, 1, 0.4330127018922193),
    (3, 4, 5, 6)
]


@pytest.mark.parametrize("side_a, side_b, side_c, area", triangle_area)
def test_triangle_area_1(side_a, side_b, side_c, area):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.area == area


triangle_perimetr = [
    (1, 1, 1, 3),
    (3, 4, 5, 12)
]


@pytest.mark.parametrize("side_a, side_b, side_c, perimetr", triangle_perimetr)
def test_triangle_area_2(side_a, side_b, side_c, perimetr):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.perimetr == perimetr


def test_triangle_add_area():
    triangle = Triangle(3, 4, 5)
    square = Square(5)
    assert triangle.add_area(square) == 31


def test_triangle_add_negative_area():
    triangle = Triangle(3, 5, 5)
    square = Square(5)
    assert triangle.add_area(square) != 31
