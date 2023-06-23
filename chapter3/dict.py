import collections
a = {'x': 1, 'y': 2}
b = dict(x=1, y=2)
c = dict(zip(['x', 'y'], [1, 2]))
d = dict([('x', 1), ('y', 2)])
e = dict({'y': 2, 'x': 1})
print(a, b, c, d, e)
print(a == b == c == d == e)

# dictcomp, dict comprehension
xs = [('a', 1), ('b', 2)]
d = {k: v for k, v in xs}
print(d)

d2 = {}
d2['a'] = 1
print(d2)

# some collections
d1 = {'a': 1, 'b': 2}
d2 = {'x': 100, 'y': 200}
d3 = {'x': 999, 'z': -1}
cm = collections.ChainMap(d1, d2, d3)
print(cm['x'])
d2['x'] *= 10
print(cm['x'])
cm['x'] *= 10
print(cm['x'])
print(d1, d2, d3, cm)

print(locals())