import functools
import math


class Vector2d:
    typecode = 'd'

    def print_method(func):
        @functools.wraps(func)
        def decorate(*args, **kwargs):
            print(f'execute {func.__name__}')
            return func(*args, **kwargs)
        return decorate

    # 把x和y变成不可变的，这样我们才可以实现自己的hash
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self) -> int:
        return hash(self.x) ^ hash(self.y)

    @print_method
    def __init__(self, x, y) -> None:
        self.__x = float(x)
        self.__y = float(y)

    # 把Vector2d变成了一个可拆包的对象，也实现了可迭代
    @print_method
    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    @print_method
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}, ({self.__x, self.__y})'

    @print_method
    def __str__(self) -> str:
        return str(tuple(self))

    @print_method
    def __eq__(self, other: object) -> bool:
        return tuple(self) == tuple(other)

    @print_method
    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    @print_method
    def __bool__(self):
        return bool(abs(self))


v1 = Vector2d(3, 4)
x, y = v1
print(v1)
print(abs(v1))
print(bool(v1))

xs = {v1: 'v1'}
print(xs)

print(v1.__dict__)
# {'_Vector2d__x': 3.0, '_Vector2d__y': 4.0}
# 这个特性叫做name mangling，名称改写。
# 防止子类和父类的名字重名，避免调试的困难。

print(v1._Vector2d__x)
# 我们可以通过这个别名来访问类的保护属性，这是允许的但是很危险。
v1._Vector2d__x = 30
print(v1._Vector2d__x)
print(v1.__dict__)
