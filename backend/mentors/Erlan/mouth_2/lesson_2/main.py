class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def info(self):
        raise NotImplementedError("This method should be overridden in subclasses")


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length**2

    def info(self):
        area = self.calculate_area()
        print(
            f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}"
        )


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        area = self.calculate_area()
        print(
            f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}"
        )


if __name__ == "__main__":
    shapes = [
        Square(5),
        Square(10),
        Rectangle(5, 8),
        Rectangle(10, 20),
        Rectangle(3, 7),
    ]

    for shape in shapes:
        shape.info()
