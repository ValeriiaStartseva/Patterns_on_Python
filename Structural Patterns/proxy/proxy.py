from abc import ABC, abstractmethod


class Milk(ABC):
    @abstractmethod
    def add(self) -> None:
        pass


class PlantMilk(Milk):
    def add(self) -> None:
        print("The plant milk was added.")


class Proxy(Milk):
    def __init__(self, plant_milk: PlantMilk) -> None:
        self._plant_milk = plant_milk

    def add(self) -> None:
        if self.check_milk():
            self._plant_milk.add()
            self.add_milk()

    def check_milk(self) -> bool:
        print("Proxy: Checking if milk was added.")
        return True

    def add_milk(self) -> None:
        print("Proxy: Add milk", end="")


def client_code(subject: Milk) -> None:
    subject.add()


print("Client: Executing the client code with a real subject:")
real_subject = PlantMilk()
client_code(real_subject)

print("Client: Executing the same client code with a proxy:")
proxy = Proxy(real_subject)
client_code(proxy)
