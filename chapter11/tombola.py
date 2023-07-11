import random
import abc
from typing import Any


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """xxx"""
    @abc.abstractmethod
    def pick(self):
        """xxx"""

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class BingoCage(Tombola):
    def __init__(self, items) -> None:
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self) -> Any:
        self.pick()


class LotteryBlower(Tombola):
    def __init__(self, items) -> None:
        self._balls = list(items)

    def load(self, items):
        self._balls.extend(items)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))
