from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # abstract method

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Usage
rect = Rectangle(5, 10)
circle = Circle(7)

print("Rectangle Area:", rect.area())  # 50
print("Circle Area:", circle.area())  # 153.86
