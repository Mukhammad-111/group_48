from curses.textpad import rectangle


class Figure:
    unit = 'см'
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, __side_length):
        super().__init__()
        self.__side_length = __side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(f'Square side_length: {self.__side_length}{self.unit}, area: {self.calculate_area()}{self.unit}')

class Rectangle(Figure):
    def __init__(self, __length, __width):
        super().__init__()
        self.__length = __length
        self.__width = __width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f'Rectangle length:{self.__length}{self.unit},'
              f' width:{self.__width}{self.unit}, area:{self.calculate_area()}{self.unit}')


square1 = Square(4)
square2 = Square(7)
rectangle1 =Rectangle(12,8)
rectangle2 =Rectangle(6,10)
rectangle3 =Rectangle(14,9)

figures_list = [square1, square2, rectangle1, rectangle2, rectangle3]

for elem in figures_list:
    elem.info()
