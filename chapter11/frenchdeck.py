from random import shuffle
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __str__(self) -> str:
        return f'{self._cards[:5]}...'

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)


d = FrenchDeck2()


shuffle(d)
print(d)
