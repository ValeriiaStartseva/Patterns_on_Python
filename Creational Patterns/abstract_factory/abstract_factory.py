from abc import ABC, abstractmethod


class ChocolateFactory(ABC):
    """
    абстрактна фабрика
    """

    @abstractmethod
    def create_dark_chocolate(self):
        pass

    @abstractmethod
    def create_milk_chocolate(self):
        pass

    @abstractmethod
    def create_with_nuts_chocolate(self):
        pass


class Roshen(ChocolateFactory):
    """
    конкретна фабрика
    """

    def create_dark_chocolate(self):
        return DarkChocolate("Roshen Dark Chocolate")

    def create_milk_chocolate(self):
        return MilkChocolate("Roshen Milk Chocolate")

    def create_with_nuts_chocolate(self):
        return WithNutsChocolate("Roshen Chocolate with Nuts")


class ABK(ChocolateFactory):
    """
    конкретна фабрика
    """
    def create_dark_chocolate(self):
        return DarkChocolate("ABK Dark Chocolate")

    def create_milk_chocolate(self):
        return MilkChocolate("ABK Milk Chocolate")

    def create_with_nuts_chocolate(self):
        return WithNutsChocolate("ABK Chocolate with Nuts")


class Konti(ChocolateFactory):
    """
    конкретна фабрика
    """

    def create_dark_chocolate(self):
        return DarkChocolate("Konti Dark Chocolate")

    def create_milk_chocolate(self):
        return MilkChocolate("Konti Milk Chocolate")

    def create_with_nuts_chocolate(self):
        return WithNutsChocolate("Konti Chocolate with Nuts")


class DarkChocolate:
    """
    product
    """
    def __init__(self, name):
        self.name = name
        print(f"Creating {self.name}")


class MilkChocolate:
    """
    product
    """
    def __init__(self, name):
        self.name = name
        print(f"Creating {self.name}")


class WithNutsChocolate:
    """
    product
    """

    def __init__(self, name):
        self.name = name
        print(f"Creating {self.name}")


roshen_factory = Roshen()

milk_chocolate = roshen_factory.create_milk_chocolate()

