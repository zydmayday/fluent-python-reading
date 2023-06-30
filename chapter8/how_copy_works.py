import copy

l1 = [1, 2, [3, 4]]
# l2只会拷贝l1的最外面一层
l2 = l1[:]

print(id(l1))
print(id(l2))

l1[-1].append(5)
print(l1, l2)

l1.append(6)
print(l1, l2)


class Bus:
    def __init__(self, xs=None) -> None:
        if xs is None:
            self.xs = []
        else:
            self.xs = xs[:]

    def __repr__(self) -> str:
        return f'bus: {self.xs}'

    def pick(self, name):
        self.xs.append(name)

    def drop(self, name):
        self.xs.remove(name)


bus1 = Bus(['A', 'B', 'C'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(bus1, bus2, bus3)
bus1.drop('A')
print(bus1, bus2, bus3)
