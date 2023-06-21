from collections import namedtuple

A = namedtuple('A1', ['a', 'b'])
print(A('xx', 'yy'))

A = namedtuple('A2', 'a b')
print(A('xx', 'yy'))