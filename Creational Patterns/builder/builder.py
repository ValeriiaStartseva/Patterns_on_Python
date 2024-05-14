from abc import ABC, abstractmethod


class BurgerBuilderInterface(ABC):
    """
    Burger Builder interface
    """

    @abstractmethod
    def add_bun(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_tomatoes(self):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient):
        pass

    @abstractmethod
    def build(self):
        pass


class BurgerBuilder(BurgerBuilderInterface):
    """
    Burger Builder
    """

    def __init__(self):
        self.burger = Burger()

    def add_bun(self) -> 'BurgerBuilder':
        self.burger.add_ingredient("Bun")
        return self

    def add_sauce(self) -> 'BurgerBuilder':
        self.burger.add_ingredient("Sauce")
        return self

    def add_tomatoes(self) -> 'BurgerBuilder':
        self.burger.add_ingredient("Tomatoes")
        return self

    def remove_ingredient(self, ingredient) -> 'BurgerBuilder':
        self.burger.remove_ingredient(ingredient)
        return self

    def build(self):
        return self.burger


class Burger:
    """
    Burger
    methods:
    add_ingredient(ingredient) -> method added ingredient to list
    remove_ingredient(ingredient) -> method removed ingredient from list
    """

    def __init__(self):
        self.ingredients: list = []

    def add_ingredient(self, ingredient) -> None:
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient) -> None:
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
        else:
            print(f"{ingredient} is not in the burger.")

    def __str__(self):
        return ", ".join(self.ingredients)


"""
testing
"""

# create builder of burger
builder = BurgerBuilder()

# add ingredients to burger
builder.add_bun().add_sauce().add_tomatoes().add_tomatoes().add_tomatoes()

# remove 1 from ingredients
builder.remove_ingredient("Tomatoes")

# make burger
burger = builder.build()

# print info
print("Constructed Burger:", burger)
