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
