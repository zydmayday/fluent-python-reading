from operator import add
import functools


def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)


print(factorial(42))
print(factorial.__doc__)

# we can assign function to a variable
fact = factorial
print(fact(5))

# we can pass function as a arugmentmap(lambda x: x * 2,
print(map(fact, range(11)))
print(list(map(fact, range(11))))

print(functools.reduce(add, range(100)) == sum(range(100)))
