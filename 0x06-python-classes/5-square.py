#!/usr/bin/python3
""" defines a class
"""


class Square:
    """ class Square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= ")
        else:
            self.size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end=)
                print()
