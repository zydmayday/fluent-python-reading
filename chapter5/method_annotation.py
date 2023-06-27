def fn(a, b: 'this is b' = 1):
    '''this is a doc of fn'''
    return a + b


print(fn.__annotations__)
