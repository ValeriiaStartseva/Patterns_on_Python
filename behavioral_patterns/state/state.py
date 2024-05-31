from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    """
    The context defines the interface and maintains a reference to an instance of a subclass of Status,
    which represents the current state of the Context.
    """

    def __init__(self, state: Status) -> None:
        self._state = None
        self.transition_to(state)

    def transition_to(self, state: Status) -> None:
        """
        Transition to a new state and set the context of the new state.
        """
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request_info(self) -> None:
        """
        Request the current state's action (info_order).
        """
        self._state.info_order()


class Status(ABC):
    """
    The base state class that declares methods which all concrete states should implement.
    """

    def __init__(self) -> None:
        self._context = None

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def info_order(self) -> None:
        pass


class NewOrder(Status):
    def info_order(self) -> None:
        print("Status: New order has been created!")
        self.context.transition_to(AcceptedOrder())


class AcceptedOrder(Status):
    def info_order(self) -> None:
        print("Status: Accepted")
        self.context.transition_to(SendOrder())


class SendOrder(Status):
    def info_order(self) -> None:
        print("Status: Order has been sent!")
        self.context.transition_to(DeliveredOrder())


class DeliveredOrder(Status):
    def info_order(self) -> None:
        print("Status: Order has been delivered!")
        self.context.transition_to(ReceivedOrder())


class ReceivedOrder(Status):
    def info_order(self) -> None:
        print("Status: Order has been received!")
        # No transition to another state as this is the final state.


# Example usage:
if __name__ == "__main__":
    # Initialize the context with the NewOrder state
    context = Context(NewOrder())

    # Simulate the state transitions
    context.request_info()  # Transition from NewOrder to AcceptedOrder
    context.request_info()  # Transition from AcceptedOrder to SendOrder
    context.request_info()  # Transition from SendOrder to DeliveredOrder
    context.request_info()  # Transition from DeliveredOrder to ReceivedOrder
    context.request_info()  # ReceivedOrder does not transition further
