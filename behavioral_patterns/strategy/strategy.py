from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    def __init__(self, strategy: TransportStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> TransportStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: TransportStrategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Calculating time and price using the strategy")
        time = self._strategy.time(1.0)
        print("Estimated time:", time)
        price = self._strategy.price()
        print("Estimated price:", price)


class TransportStrategy(ABC):
    @abstractmethod
    def time(self, km: float) -> float:
        pass

    @abstractmethod
    def price(self) -> float:
        pass


class CarStrategy(TransportStrategy):
    def time(self, km: float) -> float:
        time = km/80
        return time

    def price(self) -> float:
        # Calculate price for car transportation
        pass


class WalkingStrategy(TransportStrategy):
    def time(self, km: float) -> float:
        time = km/5
        return time

    def price(self) -> float:
        # Calculate price for walking transportation
        pass


# testing
context = Context(CarStrategy())
print("Client: Strategy is set to car transportation.")
context.do_some_business_logic()
