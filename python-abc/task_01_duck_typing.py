#!/usr/bin/python3
"""
Module for Shape, Circle and Rectangle
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract class Shape
    """
    @abstractmethod
    def area(self):
        """
        Abstract method area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method perimeter
        """
        pass


class Circle(Shape):
    """
    Circle class
    """
    def __init__(self, radius):
        """
        Initializes Circle
        """
        self.radius = radius

    def area(self):
        """
        Returns area of circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Returns perimeter of circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        Initializes Rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns perimeter of rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints area and perimeter of shape
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
