import json
from typing import Dict
from typing import List, Union, TypedDict


class FlowerState(TypedDict):
    name: str
    color: str


class Flower:
    def __init__(self, name: str, color: str) -> None:
        self._name = name
        self._color = color

    def display(self, price: float, availability: bool) -> None:
        name = json.dumps(self._name)
        color = json.dumps(self._color)
        print(f"Flower: {name}, Color: {color}, Price: {price}, Available: {availability}")


class FlowerFactory:
    _flowers: Dict[str, Flower] = {}

    def __init__(self, initial_flowers: List[Union[FlowerState, dict]]) -> None:
        for state in initial_flowers:
            key = self.get_key(state)
            self._flowers[key] = Flower(*state)

    @staticmethod
    def get_key(state: Dict[str, str]) -> str:
        return "_".join(sorted(state.values()))

    def get_flower(self, shared_state: Dict[str, str]) -> Flower:
        key = self.get_key(shared_state)

        if key not in self._flowers:
            print("FlowerFactory: Can't find a flower, creating new one.")
            self._flowers[key] = Flower(*shared_state)
        else:
            print("FlowerFactory: Reusing existing flower.")

        return self._flowers[key]

    def list_flowers(self) -> None:
        count = len(self._flowers)
        print(f"FlowerFactory: I have {count} flowers:")
        for flower in self._flowers.values():
            print(flower._name, flower._color)


def add_flower_to_shop(
    factory: FlowerFactory, name: str, color: str,
    price: float, availability: bool
) -> None:
    print("\n\nFlower Shop: Adding a flower to inventory.")
    flower = factory.get_flower({"name": name, "color": color})
    flower.display(price, availability)


if __name__ == "__main__":
    factory = FlowerFactory([
        {"name": "Rose", "color": "Red"},
        {"name": "Tulip", "color": "Yellow"},
        {"name": "Lily", "color": "White"},
    ])

    factory.list_flowers()

    add_flower_to_shop(
        factory, "Rose", "Red", 10.0, True)

    add_flower_to_shop(
        factory, "Tulip", "Yellow", 8.0, False)

    print("\n")

    factory.list_flowers()
