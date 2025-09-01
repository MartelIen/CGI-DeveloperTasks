import argparse
import json
import sys

from abc import ABC, abstractmethod
from typing import List, Dict, Type
import math


class Shape(ABC):
    """Abstract base class for calulating the area of shapes."""

    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area of the shape."""
        pass


class Circle(Shape):
    """Circle shape with a given radius."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return math.pi * self.radius**2


class Rectangle(Shape):
    """Rectangle shape with width and height."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.height


class Triangle(Shape):
    """Triangle shape with base and height."""

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        """Return the area of the triangle."""
        return 0.5 * self.base * self.height


SHAPE_DICT: Dict[str, Type[Shape]] = {
    "circle": Circle,
    "rectangle": Rectangle,
    "triangle": Triangle,
}


def create_shape(shape_dict: dict) -> Shape:
    """Create a Shape instance from a dictionary."""
    shape_type = shape_dict.get("type")
    cls = SHAPE_DICT.get(shape_type)

    if not cls:
        raise ValueError(f"Unknown shape type: {shape_type}")

    params = {k: v for k, v in shape_dict.items() if k != "type"}
    try:
        return cls(**params)
    except TypeError as e:
        raise ValueError(f"Invalid parameters for {shape_type}: {e}")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate total area of shapes from a JSON file."
    )
    parser.add_argument("--file", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        with open(args.file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        sys.exit(1)

    shapes: List[Shape] = []
    shape_counts: Dict[str, int] = {}
    for item in data:
        try:
            shape = create_shape(item)
            shapes.append(shape)
            t = item["type"]
            shape_counts[t] = shape_counts.get(t, 0) + 1
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    total_area = sum(s.area() for s in shapes)
    result = f"Total area: {total_area:.1f}"
    print(result)
    with open("area.txt", "w", encoding="utf-8") as f:
        f.write(f"{result}\n")

    # Bonus - print shape count
    for t, count in shape_counts.items():
        print(f"{t.capitalize()}s: {count}")


if __name__ == "__main__":
    main()
