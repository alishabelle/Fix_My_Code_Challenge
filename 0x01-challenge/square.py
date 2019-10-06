#!/usr/bin/python3
""" building class square """


class Square():
    """ creating area and parameter for square output """

    width = 0
    height = 0

    def __init__(self, width, height):
        """ defining the square """
        if width == height:
            self.width = width
            self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ perimeter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ printing out the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
