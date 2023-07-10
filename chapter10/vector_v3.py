from array import array
import math
import numbers
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

    def __len__(self):
        return len(self._xs)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._xs[index])
        elif isinstance(index, numbers.Integral):
            return self._xs[index]
        else:
            raise TypeError(f'{cls.__name__} indices must be integers')


# %%
v1 = Vector(range(10))
print(repr(v1))

print(repr(v1[2:5]))
print(repr(v1[-1]))
print(repr(v1['a']))

# %%
print(sum([x for x in [1, 2, 3]]))
# 这个是使用了生成器表达式
print(sum(x for x in [1, 2, 3]))

# %%
