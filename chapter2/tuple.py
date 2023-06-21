# use placeholder
a, b, _ = (1, 2, 3)
print(a, b)

args = (1, 2)


def add(a, b):
    return a+b


# unpack tuple to pass arguments
print(add(*args))

# use *args to get all rest of items in tuple
x, y, *rest = (1, 2, 3, 4, 5)
print(x, y, rest)

# even in the middle
x, *rest, y = (1, 2, 3, 4, 5)
print(x, y, rest)

# nested
a, b, (c, d) = (1, 2, (3, 4))
print(a, b, c, d)

a, (c, d), b = (1, (3, 4), 2)
print(a, b, c, d)
