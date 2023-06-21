s = '123456'
print(s[:2])
print(s[2:])

s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

# named slice
_reverse = slice(None, None, -1)
print(s[_reverse])

xs = [[1, 2, 3], [4, 5, 6]]
# numpy supports such syntax
# print(xs[1, 2])

xs = list(range(10))
print(xs)

xs[2:4] = [99, 100]
print(xs)

xs[2:4] = [10000]
print(xs)

a = [1, 2, 3]
b = a * 3
print(a, b)
a[2] = 99
# b will not be modified
print(a, b)

a = [1, 2, 3]
b = [a] * 3
a[2] = 999
# modify a will make b be modified
print(a, b)
b[0][0] = 123
# even modify any items in b will affect to all items
print(a, b)

l = [1, 2, 3]
print(id(l))
l *= 2
print(id(l))

# t = (1, 2, [3, 4])
# t[2] += [5, 6]
# print(t)

l = [1, 2, [3, 4]]
l[2] += [5, 6]
print(l)

# array.array is faster than builtin list

# how to use memoryview
