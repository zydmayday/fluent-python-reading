class MutableArgs:
    def __init__(self, xs=[]) -> None:
        self.xs = xs

    def __repr__(self) -> str:
        return f'MutableArgs: {self.xs}'

    def pick(self, x):
        self.xs.append(x)

    def drop(self, x):
        self.xs.remove(x)


ma1 = MutableArgs()
ma1.pick('A')
print(ma1)

# ma2 will have 'A' in its self.xs
ma2 = MutableArgs()
print(ma1, ma2)
