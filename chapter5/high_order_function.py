xs = ['aa', 'b', 'ccccc', 'dddd', 'eee']
print(sorted(xs, key=len))

print(list(filter(lambda x: x % 2, range(10))))
print(list(map(lambda x: x * 2, filter(lambda x: x % 2, range(10)))))
