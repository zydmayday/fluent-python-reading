import time


def clock(prefix):
    def decorate(func):
        def clocked(*args):
            start = time.time()
            result = func(*args)
            elapsed = time.time() - start
            print(f'{prefix}func {func.__name__}{args} -> {result} elapsed {elapsed}')
            return result
        return clocked
    return decorate


@clock('T_T ')
def foo(a, b):
    return a + b


foo(1, 2)
foo(40, 2)
