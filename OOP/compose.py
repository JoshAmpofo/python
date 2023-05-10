#!/usr/bin/env python3
"""Composing and aggregating a class"""

#class Point:
#    """Defines cartesian axes"""
#    def __init__(self, x, y):
#        """initialize Point

#        Args:
#            x (int): cartesian value x
#            y (int): cartesian value y
#        """
#        self.x = x
#        self.y = y

#class Shape:
#    """Defines the shape of an object along cartesian plane"""
#    def __init__(self, points):
#        """initialize shape"""
#        self.points = points


#triangle = Shape([
#    Point(0, 0),
#    Point(5, 5),
#    Point(2, 4)
#])

#print(triangle)
#print(triangle.points)

#bottom_left = Point(10, 0)
#bottom_right = Point(20, 0)
#top_left = Point(0, 10)
#top_right = Point(0, 20)

#rectangle = Shape([bottom_left, bottom_right, top_left, top_right])
#print(rectangle)
#print(rectangle.points)

#class Bill():
#    def __init__(self, description):
#        self.description = description

#class Tail():
#    def __init__(self, length):
#        self.length = length

#class Duck():
#    def __init__(self, bill, tail):
#        self.bill = bill
#        self.tail = tail

#    def about(self):
#        print('This duck has a', self.bill.description, 'bill and a',
#                self.tail.length, 'tail')

#a_tail = Tail('long')
#a_bill = Bill('wide orange')
#duck = Duck(a_bill, a_tail)
#duck.about()

####################################################################
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)
