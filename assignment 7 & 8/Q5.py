class Shape:
    def area(self):
        pass
    def peri(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
    def peri(self):
        return 2 * (self.l + self.w)

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
    def peri(self):
        return 2 * 3.14 * self.r

# Taking user input for Rectangle dimensions
l = float(input(" \n Enter the length of the rectangle: "))
w = float(input("\n Enter the width of the rectangle: "))
r = Rectangle(l, w)

# Taking user input for Circle radius
radius = float(input(" \n Enter the radius of the circle: "))
c = Circle(radius)

# Printing the area and perimeter of both shapes
print(f" \n Rectangle Area: {r.area()} and Perimeter: {r.peri()}")
print(f" \n Circle Area: {c.area()} and  Perimeter: {c.peri()}")
print("\n") 