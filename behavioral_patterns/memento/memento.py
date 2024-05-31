from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict


class OriginatorCart:
    """
    The creator contains the state of the cart.
    Method for saving state within a memento and a method restoring the state from it.
    """

    def __init__(self) -> None:
        self._state: Dict[str, int] = {}      # dict for cart
        print(f"Originator: My initial state is empty.")

    def add_item(self, item: str, quantity: int) -> None:
        """
        Add product to the cart, if product already exists in cart - plus to quantity
        """
        if item in self._state:
            self._state[item] += quantity
        else:
            self._state[item] = quantity
        print(f"Originator: Added {quantity} of {item}. Current state: {self._state}")

    def remove_item(self, item: str, quantity: int) -> None:
        """
        Remove product from the cart, if quantity <= 0, remove the product from the cart
        """
        if item in self._state:
            self._state[item] -= quantity
            if self._state[item] <= 0:
                del self._state[item]
        print(f"Originator: Removed {quantity} of {item}. Current state: {self._state}")

    def save(self) -> MementoInterface:
        """
        Save state of cart to the memento
        """
        return ConcreteMemento(self._state.copy())

    def restore(self, memento: MementoInterface) -> None:
        """
        Restore state from memento
        """
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class MementoInterface(ABC):
    """
    Interface for mementos
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

    @abstractmethod
    def get_state(self) -> Dict[str, int]:
        pass


class ConcreteMemento(MementoInterface):
    def __init__(self, state: Dict[str, int]) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> Dict[str, int]:
        """
        Method that returns the state of the memento
        """
        return self._state

    def get_name(self) -> str:
        """
        Name of memento is data + items
        """
        items_summary = ", ".join(f"{item}: {quantity}" for item, quantity in self._state.items())
        return f"{self._date} / ({items_summary})"

    def get_date(self) -> str:
        return self._date


class Caretaker:
    """
    Works with all mementos through the basic interface.
    """

    def __init__(self, originator: OriginatorCart) -> None:
        self._mementos: List[MementoInterface] = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo_cart(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        self._originator.restore(memento)

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


# testing

originator = OriginatorCart()
caretaker = Caretaker(originator)

originator.add_item("Apple", 3)
caretaker.backup()

originator.add_item("Banana", 2)
caretaker.backup()

originator.add_item("Orange", 5)
caretaker.backup()

originator.remove_item("Apple", 1)
caretaker.backup()

caretaker.show_history()

print("\nClient: Now, let's rollback!\n")
caretaker.undo_cart()

