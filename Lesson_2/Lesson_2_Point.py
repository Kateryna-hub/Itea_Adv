class Point:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '{}, {}, {}'.format(self.x, self.y, self.z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z + other.z)


    def __mul__(sefl, other):
        return Point(sefl.x * other.x, sefl.y * other.y, sefl.z * other.z)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y, self.z / other.z)


    def __pos__(self):
        return Point(self.x, self.y, self.z)

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)



a = Point(1, 2, 3)
b = Point(1,2,3)
c = Point(8,4,3)
print(a + b+ c)
print(a * b)
print(a + c - b)
print(a / b)
print(-a)
print(-a.x)

