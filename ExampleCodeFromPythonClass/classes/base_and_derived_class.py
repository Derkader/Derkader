class Shape:
    """Shape class"""
    colors = ['BLUE', 'GREEN', 'ORANGE', 'PURPLE', 'RED', 'YELLOW']

    def __init__(self, color='BLUE'):
        if color not in self.colors:
            raise InvalidColorError
        self.color = color

    def change_color(self, new_color):
        if new_color not in self.colors:
            raise InvalidColorError
        self.color = new_color

    def display_color(self):
        return str(self.color)


class InvalidColorError(Exception):
    """InvalidColorError is derived class of Excpetion base class"""
    pass


class Rectangle(Shape):  # Base class is Shape
    """Rectangle derived class of Shape base class"""

    def __init__(self, c='RED', l=0, w=0):  # default values
        super().__init__(c)  # calls the base constructor
        if l < 0 or w < 0:
            raise ValueError
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def display_color(self):
        return str('Rectangle color ' + self.color)


if __name__ == '__main__':

    # Driver
    my_shape = Shape()
    my_rectangle = Rectangle()
    # Tests if object my_shape is Shape
    print('my_shape is a Shape:', isinstance(my_shape, Shape))
    # Tests if object my_rectangle is Shape
    print('my_rectangle is a Shape:', isinstance(my_rectangle, Shape))
    # Tests if object my_shape is Rectangle
    print('my_shape is a Rectangle:', isinstance(my_shape, Rectangle))
    # Tests if object my_rectangle is Rectangle
    print('my_rectangle is a Rectangle:', isinstance(my_rectangle, Rectangle))

    # Driver with setting values
    r = Rectangle(l=3, w=4.5)
    try:
        r.change_color('PURPLE')
    except InvalidColorError:
        print('Invalid color, color not changed!')
        print('Rectangle color:', r.display_color())
        print('The area of length,', r.length, 'and width', r.width, 'is', r.area())
