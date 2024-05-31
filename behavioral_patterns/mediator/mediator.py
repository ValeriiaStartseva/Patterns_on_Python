from __future__ import annotations
from abc import ABC, abstractmethod


class Mediator(ABC):
    """
    Abstract interface for mediators
    """

    @abstractmethod
    def ordering(self, sender: object, order: str) -> None:
        pass


class WaiterMediator(Mediator):
    """
    Concrete implementation of mediator for waiter
    """
    def __init__(self, component1: CookerComponent1, component2: CookerComponent2) -> None:
        self._component1 = component1
        self._component1.mediator = self    # this code set waiter as mediator between comp1 and comp2
        self._component2 = component2
        self._component2.mediator = self    # this code set waiter as mediator between comp1 and comp2

    def ordering(self, sender: object, order: str) -> None:
        if order == "Menu 1":
            print("Mediator reacts on menu 1 and gives cooker task to make menu A:")
            self._component1.order_menu_a()
        elif order == "Menu 2":
            print("Mediator reacts on menu 2 and gives cooker task to make menu C:")
            self._component2.order_menu_c()


class BaseComponent:
    """
    Base Component
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class CookerComponent1(BaseComponent):
    def order_menu_a(self) -> None:
        print("Cooker 1 does Menu A.")
        if self.mediator:
            self.mediator.ordering(self, "A")

    def order_menu_b(self) -> None:
        print("Cooker 1 does Menu B.")
        if self.mediator:
            self.mediator.ordering(self, "B")


class CookerComponent2(BaseComponent):
    def order_menu_c(self) -> None:
        print("Cooker 2 does Menu C.")
        if self.mediator:
            self.mediator.ordering(self, "C")

    def order_menu_d(self) -> None:
        print("Cooker 2 does Menu D.")
        if self.mediator:
            self.mediator.ordering(self, "D")


# testing

c1 = CookerComponent1()
c2 = CookerComponent2()
mediator = WaiterMediator(c1, c2)

print("Client orders menu 1.")
mediator.ordering(None, "Menu 1")

print("Client orders menu 2.")
mediator.ordering(None, "Menu 2")
