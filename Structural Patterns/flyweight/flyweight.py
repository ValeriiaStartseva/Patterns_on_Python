from typing import Dict


class FlowerFlyweight:
    def __init__(self, color: str) -> None:
        self._color: str = color

    def display(self, name: str, price: float, availability: bool) -> None:
        print(f"Flower: {name}, Color: {self._color}, Price: {price}, Available: {availability}")


class FlowerFactory:
    _flyweights: Dict[str, FlowerFlyweight] = {}

    def get_flyweight(self, color: str) -> FlowerFlyweight:
        if color not in self._flyweights:
            self._flyweights[color] = FlowerFlyweight(color)
        return self._flyweights[color]


class Flower:
    def __init__(self, name: str, flyweight: FlowerFlyweight) -> None:
        self._name = name
        self._flyweight = flyweight

    def display(self, price: float, availability: bool) -> None:
        self._flyweight.display(self._name, price, availability)


def add_flower_to_shop(factory: FlowerFactory, name: str, color: str, price: float, availability: bool) -> None:
    print("\n\nFlower Shop: Adding a flower to inventory.")
    flyweight = factory.get_flyweight(color)
    flower = Flower(name, flyweight)
    flower.display(price, availability)


# testing

factory_test = FlowerFactory()

add_flower_to_shop(factory_test, "Rose", "Red", 10.0, True)
add_flower_to_shop(factory_test, "Tulip", "Yellow", 8.0, False)
