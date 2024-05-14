import copy


class Shape:
    """
    Base class for all shapes
    method clone make deepcopy of shape
    method draw shape drawing figure
    """

    def __init__(self):
        self.type = None

    def clone(self):
        return copy.deepcopy(self)

    def draw_shape(self):
        pass


class Rectangle(Shape):
    """
    Specific class for rectangle
    """

    def __init__(self, width: int, height: int):
        super().__init__()
        self.type: str = "Rectangle"
        self.width: int = width
        self.height: int = height

    def draw(self) -> None:
        print(f"Drawing a {self.type} with width {self.width} and height {self.height}")


class Circle(Shape):
    """
    Specific class for circle
    """

    def __init__(self, radius: int):
        super().__init__()
        self.type: str = "Circle"
        self.radius: int = radius

    def draw(self) -> None:
        print(f"Drawing a {self.type} with radius {self.radius}")


# create prototype for shape
rectangle_prototype = Rectangle(10, 5)
circle_prototype = Circle(7)

# Cloning prototypes to create new figures
rectangle = rectangle_prototype.clone()
circle = circle_prototype.clone()

# Drawing cloned shapes
rectangle.draw()
circle.draw()


