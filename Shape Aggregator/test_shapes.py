import pytest
import math
from main import Circle, Rectangle, Triangle, create_shape

def test_circle_area():
    c = Circle(2)
    assert pytest.approx(c.area(), 0.01) == math.pi * 4

def test_rectangle_area():
    r = Rectangle(3, 5)
    assert r.area() == 15

def test_triangle_area():
    t = Triangle(4, 6)
    assert t.area() == 12

def test_create_shape_circle():
    d = {"type": "circle", "radius": 3}
    s = create_shape(d)
    assert isinstance(s, Circle)
    assert pytest.approx(s.area(), 0.01) == math.pi * 9

def test_create_shape_rectangle():
    d = {"type": "rectangle", "width": 2, "height": 8}
    s = create_shape(d)
    assert isinstance(s, Rectangle)
    assert s.area() == 16

def test_create_shape_triangle():
    d = {"type": "triangle", "base": 10, "height": 2}
    s = create_shape(d)
    assert isinstance(s, Triangle)
    assert s.area() == 10

def test_create_shape_invalid_type():
    d = {"type": "hexagon", "side": 2}
    with pytest.raises(ValueError):
        create_shape(d)

def test_create_shape_missing_param():
    d = {"type": "circle"}
    with pytest.raises(ValueError):
        create_shape(d)
        
