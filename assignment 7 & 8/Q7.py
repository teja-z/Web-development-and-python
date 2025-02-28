import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rot(self):
        return math.atan2(self.y, self.x)

    def dist(self, o):
        return math.sqrt((self.x - o.x)**2 + (self.y - o.y)**2)

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

x1 = float(input("Enter x for 2D vector: "))
y1 = float(input("Enter y for 2D vector: "))
print("\n")
v1 = Vector2D(x1, y1)

x2 = float(input("Enter x for 3D vector: "))
y2 = float(input("Enter y for 3D vector: "))
z2 = float(input("Enter z for 3D vector: "))
print("\n")
v2 = Vector3D(x2, y2, z2)

print(v1.mag(), v2.mag())
print("\n")