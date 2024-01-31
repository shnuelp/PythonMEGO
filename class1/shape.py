class Shape():

    def __init__(self, color):
        self.color = color

    def area(self):
            raise NotImplementedError("Subclasses must implement the area() method")

    def display_info(self):
        print( f"The color is: {self.color}")


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self):
          return 3.14 * self.radius ** 2


    def display_info(self):
        super().display_info()
        print( f"The radius: {self.radius} \n the area is :{self.area()}")


class Rectangle(Shape):

    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def display_info(self):
       super().display_info()
       print( f"The length {self.length}\nThe wibth: {self.width:}\nthe area is: {self.area()}")

# testing
# circle = Circle("green", 3)
#
# circle.display_info()
# #
Rectangle = Rectangle("green", 10, 10)
Rectangle.display_info()