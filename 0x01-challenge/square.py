#!/usr/bin/python3
"""
creating a new class (Square)
"""


class Square():
    """creating the square class area + perimeter"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """instantiate the square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ to get the area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ to get the perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ printing out the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
