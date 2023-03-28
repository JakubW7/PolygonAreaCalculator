import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture'
        else:
            for i in range(self.height):
                picture += self.width * "*" + '\n'
            return picture

    def get_amount_inside(self, fig):
        return math.floor(self.width / fig.width) * math.floor(self.height / fig.height)


class Square(Rectangle):

    def __init__(self, side=0, width=0, height=0):
        super().__init__(width, height)
        if side != 0:
            self.width = side
            self.height = side

    def __str__(self):
        return 'Square(side={})'.format(self.width)

    def set_width(self, width):
        Rectangle.set_width(self, width)
        self.height = width

    def set_height(self, height):
        Rectangle.set_height(self, height)
        self.width = height

    def set_side(self, side):
        self.width = side
        self.height = side
