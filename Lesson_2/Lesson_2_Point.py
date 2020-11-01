class Point:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '{}, {}, {}'.format(self.x, self.y, self.z)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z + other.z

    def __mul__(sefl, other):
        return sefl.x * other.x, sefl.y * other.y, sefl.z * other.z

    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y, self.z / other.z


    def __pos__(self):
        return self.x, self.y, self.z

    def __neg__(self):
        return -self.x, -self.y, -self.z



a= Point(1,2,3)
b = Point(1,2,3)
print(a + b)
print(a * b)
print(a - b)
print(a / b)
print(-a)
print(-a.x)

