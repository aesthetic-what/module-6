from math import pi


class Figure:
    """
    Figure(color: (r: int, g: int, b: int), *sides: int)
    Если число сторон не совпадает с количеством сторон и цвет недопустим,
    то будет длина 1, цвет (0,0,0)
    """

    filled = True
    __sides = []
    __color = (0, 0, 0)

    def __init__(self, color, *sides):
        if self.__is_valid_sides(*sides):
            if self.sides_count != len(sides):
                self.__sides = [sides[0]] * self.sides_count
            else:
                self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        if self.__is_valid_color(color):
            self.set_color(color[0], color[1], color[2])
        else:
            self.set_color(0, 0, 0)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        return 0 <= color[0] <= 255 and 0 <= color[1] <= 255 and 0 <= color[2] <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color((r, g, b)):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        if self.sides_count == len(sides):
            for x in sides:
                if x <= 0:
                    return False
                return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) and len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    """
    Circle(color: (r: int, g: int, b: int), circumference: int)
    """
    sides_count = 1
    __radius = 0  # l=2*pi*r r=l/(2*pi)

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius * self.__radius


class Triangle(Figure):
    """
    Triangle(color: (r: int, g: int, b: int), *sides: int)
    """
    sides_count = 3
    __height = 0  # h=2*s/b)

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.get_square() * 2 / self.get_sides()[1]

    def get_square(self):  # s=(p/2*(p/2-a)*(p/2-b)*(p/2-c))**0.5
        return (len(self) / 2 * (len(self) / 2 - self.get_sides()[0]) *
                (len(self) / 2 - self.get_sides()[1]) * (len(self) / 2 - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    """
    Cube(color: (r: int, g: int, b: int), *sides: int)
    """
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 12 or len(sides) == 1:  # задали 1 или 12 сторон, но они должны быть равны
            self.__sides = [sides[0]] * 12
            super().__init__(color, *self.__sides)
        else:
            super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

