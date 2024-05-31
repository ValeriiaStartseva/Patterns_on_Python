from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: BooksCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class BooksCollection(Iterable):
    def __init__(self, collection: list[Any] = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)


# testing
collection = BooksCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

print("Straight traversal:")
for item in collection:
    print(item)
print("")

print("Reverse traversal:")
for item in collection.get_reverse_iterator():
    print(item)
