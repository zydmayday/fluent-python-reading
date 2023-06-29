import functools
import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'func {func.__name__}{args} elapsed {elapsed}')
        return result
    return clocked


@functools.lru_cache() # this will cache the result
@clock
def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)


fibonacci(42)
