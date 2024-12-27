class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14159 * self.radius
rectangle = Rectangle(10,2)
circle = Circle(10)
print("Area of Rectangle",rectangle.area())
print("Area of Circle",circle.area(),"\nPerimeter of Circle",circle.perimeter())