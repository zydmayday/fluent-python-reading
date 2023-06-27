import random
from typing import Any

class BingoCage:
  def __init__(self, items) -> None:
    self._items = list(items)
    random.shuffle(self._items)
  
  def pick(self):
    try:
      return self._items.pop()
    except IndexError:
      raise LookupError('pick from empty BingoCage')

  def __call__(self, *args: Any, **kwds: Any) -> Any:
    return self.pick()

bingo = BingoCage(range(10))
print(bingo.pick())
print(bingo())
print(callable(bingo))
print(callable(bingo.pick))