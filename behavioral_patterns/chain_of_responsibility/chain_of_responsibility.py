from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового класса
    обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Возврат обработчика отсюда позволит связать обработчики простым
        # способом, вот так:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""


class Engineer(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "engineer":
            return f"Our {request} will contact you"
        else:
            return super().handle(request)


class Manager(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "manager":
            return f"Our {request} will contact you"
        else:
            return super().handle(request)


class Head(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "head":
            return f"Our {request} will contact you"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    Обычно клиентский код приспособлен для работы с единственным обработчиком. В
    большинстве случаев клиенту даже неизвестно, что этот обработчик является
    частью цепочки.
    """

    for request in ["engineer", "manager", "head"]:
        print(f"\nWhich one from the specialist you need to contact {request}?")
        result = handler.handle(request)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {request} was left untouched.", end="")


if __name__ == "__main__":
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