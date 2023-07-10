from array import array
import math
import reprlib


class Vector:
    typecode = 'd'

    def __init__(self, xs) -> None:
        self._xs = array(self.typecode, xs)

    def __iter__(self):
        return iter(self._xs)

    def __repr__(self) -> str:
        xs = reprlib.repr(self._xs)
        xs = xs[xs.find('['):-1]
        return f'Vector({xs})'

    def __str__(self) -> str:
        return str(tuple(self))

    def __eq__(self, other: object) -> bool:
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))


v1 = Vector(range(10))
print(repr(v1))

