from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class TransportComponent(ABC):
    """
    The Component interface declares an `accept` method that should take the
    base visitor interface as an argument.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class Car(TransportComponent):
    """.
    Same here: visitConcreteComponent - Car
    """

    def accept(self, visitor):
        visitor.visit_car(self)


class Bicycle(TransportComponent):
    """
    Same here: visitConcreteComponent - Bicycle
    """

    def accept(self, visitor):
        visitor.visit_bicycle(self)


class Visitor(ABC):
    """
    The Visitor Interface declares a set of visiting methods that correspond to
    component classes. The signature of a visiting method allows the visitor
    to identify the exact class of the component being visited.
    """

    @abstractmethod
    def visit_car(self, element: Car) -> None:
        pass

    @abstractmethod
    def visit_bicycle(self, element: Bicycle) -> None:
        pass


class Inspector(Visitor):
    def visit_car(self, car):
        print("Inspecting car...")

    def visit_bicycle(self, bicycle):
        print("Inspecting bicycle...")


def client_code(components: List[TransportComponent], visitor: Visitor) -> None:
    """
    The client code can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    for component in components:
        component.accept(visitor)


if __name__ == "__main__":
    components = [Car(), Bicycle()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = Inspector()
    client_code(components, visitor1)
