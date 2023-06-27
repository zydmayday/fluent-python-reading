import operator
import functools


def fact(n):
    return functools.reduce(lambda x, y: x*y, range(1, n+1))


print(fact(10))


def fact(n):
    return functools.reduce(operator.mul, range(1, n+1))


print(fact(10))

triple = functools.partial(operator.mul, 3)
print(triple(7))


def foo(a, b, c=1):
    return a+b+c


bar = functools.partial(foo)
print(bar)
# print(bar(1)) you can not pass partial arguments
print(bar(1, 2))
