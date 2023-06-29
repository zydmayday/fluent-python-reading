import time
b = 6


def f1(a):
    print(a)
    print(b)


f1(3)


def f2(a):
    print(a)
    # print(b) this will cause UnboundLocalError
    b = 6


f2(3)


def make_averager():
    xs = []

    def averager(v):
        xs.append(v)
        return sum(xs)/len(xs)
    return averager


avg = make_averager()
print(avg(1))
print(avg(2))
print(avg(3))

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

# use closure to implement decorator


def clock(func):
    def clocked(*args):
        start = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - start
        print(f'func {func.__name__}{args} elapsed {elapsed}')
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


snooze(2)
