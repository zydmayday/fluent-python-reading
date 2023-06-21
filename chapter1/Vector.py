from math import hypot


class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x},{self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        print('Vector add')
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(abs(v1))
print(v1+v2)
