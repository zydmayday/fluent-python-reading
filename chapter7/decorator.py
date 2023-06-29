def deco(func):
    print('deco executed')
    return func


@deco
def foo():
    print('foo executed')


@deco
def bar():
    print('bar executed')


# decorator will be executed immediately before other functions
foo()
bar()
