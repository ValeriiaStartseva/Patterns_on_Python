from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class NewsChannelSubject(ABC):
    """
    Interface to subscribe to news channels
    """

    @abstractmethod
    def send_by_email(self, observer: Observer) -> None:
        """
        send news to subscribers by emails
        """
        pass

    @abstractmethod
    def post_to_tg(self, observer: Observer) -> None:
        """
        post news in Telegram channel
        """
        pass

    @abstractmethod
    def send_by_sms(self, observer: Observer) -> None:
        """
        Send news to subscribers using sms
        """
        pass

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def get_state(self) -> int:
        """
        Get the current state of the news channel.
        """
        pass


class ConcreteSubject(NewsChannelSubject):
    """
    """

    _state: int = None  # state of News Channel

    _observers: List[Observer] = []  # list of subscribers

    def send_by_email(self, observer: Observer) -> None:
        """
        send news to subscribers by emails
        """
        print(f"Sending news to {observer}")

    def post_to_tg(self, observer: Observer) -> None:
        """
        post news in Telegram channel
        """
        print(f"Posting news to Telegram channel")

    def send_by_sms(self, observer: Observer) -> None:
        """
        Send news to subscribers using sms
        """
        print(f"Sending news to {observer}")

    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        self._observers.remove(observer)

    def get_state(self) -> int:
        """
        Get the current state of the news channel.
        """
        return self._state


class Observer(ABC):
    """
    Interface for observer
    """

    @abstractmethod
    def update(self, subject: NewsChannelSubject) -> None:
        """
        getting update
        """
        pass


class SubscribersObserverA(Observer):
    def update(self, subject: NewsChannelSubject) -> None:
        if subject.get_state() < 3:
            print("SubscribersObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: NewsChannelSubject) -> None:
        if subject.get_state() == 0 or subject.get_state() >= 2:
            print("ConcreteObserverB: Reacted to the event")


# testing

subject = ConcreteSubject()

observer_a = SubscribersObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)


subject._state = 2
subject.send_by_email(observer_a)
subject.post_to_tg(observer_b)
subject.send_by_sms(observer_a)

subject._state = 4
subject.send_by_email(observer_a)
subject.post_to_tg(observer_b)
subject.send_by_sms(observer_a)
