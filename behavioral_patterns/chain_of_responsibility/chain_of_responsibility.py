from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class HandlerAbstract(ABC):
    """
    Interface for handler
    """

    @abstractmethod
    def set_next(self, handler: HandlerAbstract) -> HandlerAbstract:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class Handler(HandlerAbstract):
    """
    Base class for specific handlers.
    Stores a reference to the next handler in the chain and defines the base processing method.
    """

    _next_handler: HandlerAbstract = None

    def set_next(self, handler: HandlerAbstract) -> HandlerAbstract:
        self._next_handler = handler
        return handler

    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        else:
            return None


class Engineer(Handler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "engineer":
            return f"Our {request} will contact you"
        else:
            return super().handle(request)


class Manager(Handler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "manager":
            return f"Our {request} will contact you"
        else:
            return super().handle(request)


class Head(Handler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "head":
            return f"Our {request} will contact you"
        else:
            return super().handle(request)


def client_code(handler: HandlerAbstract) -> None:
    """
    This code demonstrate how to handle client codes
    """

    for request in ["engineer", "manager", "head"]:
        print(f"\nWhich one from the specialist you need to contact {request}?")
        result = handler.handle(request)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {request} was left untouched.", end="")


engineer = Engineer()
manager = Manager()
head = Head()

engineer.set_next(manager).set_next(head)

# Клиент должен иметь возможность отправлять запрос любому обработчику, а не
# только первому в цепочке.
print("Chain: engineer > manager > head")
client_code(engineer)
print("\n")

print("Subchain: manager > head")
client_code(manager)
