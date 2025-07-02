class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def __mul__(self, other):
        return Vector(self.i * other.i, self.j * other.j, self.k * other.k)

    def __str__(self):
        return f"({self.i}i, {self.j}j, {self.k}k)"

c = Vector(2, 3, 4)
d = Vector(4, 5, 6)

print(c * d) 
print(c + d)
