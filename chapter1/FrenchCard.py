from math import hypot
import collections
from random import choice

Cards = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        print('init FrenchDeck')
        self._cards = [Cards(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        print('len FrenchDeck')
        return len(self._cards)

    def __getitem__(self, position):
        print('getitem FrenchDeck')
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))
print(deck[0])

print(choice(deck))

print(deck[:3])

print(Cards('Q', 'spades') in deck)


class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x},{self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        print('Vector add')
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(abs(v1))
print(v1+v2)
