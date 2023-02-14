#!/usr/bin/python3
"""Composing a class"""

class Point:
    """Defines cartesian axes"""
    def __init__(self, x, y):
        """initialize Point

        Args:
            x (int): cartesian value x
            y (int): cartesian value y
        """
        self.x = x
        self.y = y

class Shape:
    """Defines the shape of an object along cartesian plane"""
    def __init__(self, points):
        """initialize shape"""
        self.points = points


triangle = Shape([
    Point(0, 0),
    Point(5, 5),
    Point(2, 4)
])

print(triangle)
print(triangle.points)

bottom_left = Point(10, 0)
bottom_right = Point(20, 0)
top_left = Point(0, 10)
top_right = Point(0, 20)

rectangle = Shape([bottom_left, bottom_right, top_left, top_right])
print(rectangle)
print(rectangle.points)
