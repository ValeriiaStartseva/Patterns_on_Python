from __future__ import annotations
from abc import ABC, abstractmethod


class CommandAbstract(ABC):
    """
    Interface for all commands
    """

    @abstractmethod
    def make_order(self) -> None:
        pass

    @abstractmethod
    def change_order(self) -> None:
        pass

    @abstractmethod
    def show_order(self) -> None:
        pass


class SimpleCommand(CommandAbstract):
    """
    class for simple commands
    """

    def __init__(self, order: str) -> None:
        self.order = order

    def make_order(self) -> None:
        pass

    def change_order(self) -> None:
        pass

    def show_order(self) -> None:
        print(f"Order: {self.order}")


class ComplexCommand(CommandAbstract):
    """

    """

    def __init__(self, receiver_k: KitchenReceiver, a: str) -> None:
        self._receiver = receiver_k
        self._a = a

    def make_order(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object")
        self._receiver.prepare_order(self._a)

    def change_order(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object")
        self._receiver.prepare_changed_order(self._a)

    def show_order(self) -> None:
        pass


class KitchenReceiver:
    """
    Class Receiver for Kitchen commands
    """
    @staticmethod
    def prepare_order(a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    @staticmethod
    def prepare_changed_order(a: str) -> None:
        print(f"\nReceiver: Changed order on ({a}.)", end="")


class ClientInvoker:
    """
    Class Invoker. Invoker send commands to Receiver
    """

    def __init__(self) -> None:
        self._make_order = None
        self._change_order = None
        self._show_order = None

    def make_order(self, command: CommandAbstract) -> None:
        self._make_order = command

    def change_order(self, command: CommandAbstract) -> None:
        self._change_order = command

    def show_order(self, command: CommandAbstract) -> None:
        self._show_order = command

    def do_something(self) -> None:
        """
        """
        if self._change_order is not None:
            print("Invoker: Do you want to change order?")
            self._change_order.change_order()

        if self._show_order is not None:
            print("Invoker: Would you like to verify?")
            self._show_order.show_order()


# testing

invoker = ClientInvoker()
invoker.make_order(SimpleCommand("Say Hi!"))
receiver = KitchenReceiver()
invoker.change_order(ComplexCommand(receiver, "Prepare order"))
invoker.do_something()



