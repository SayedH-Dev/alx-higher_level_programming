#!/usr/bin/python3
""" Rectangle class definition """


class Rectangle:
    """class that represent a rectangle
    Att:
        - int number_of_instances: number of the rectangle instances
        - print_symbol: symbol to represent string
        """
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ rectangle initialization
        Args:
            - int width: rectangle width, default 0
            - int height: rectangle height, default 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method fot width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method fot height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ string of a rectangel """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = [str(self.print_symbol) * self.__width] * self.__height
        return "\n".join(row)

    def __repr__(self):
        """ string to recreate the object """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ print message when object/instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares 2 rectangles based on their areas
        Args:
            - rect_1: first rectangle
            - rect_2: second rectangle
        Return:
            - the bigger recangle or equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
