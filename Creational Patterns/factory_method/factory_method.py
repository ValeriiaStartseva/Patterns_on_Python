from abc import ABC, abstractmethod


class Pizza(ABC):
    """
    Abstract class for pizzas.
    Initializes name of pizza and method for creating pizzas
    """
    def __init__(self, name):
        self.name: str = name

    def __str__(self):
        return f"Pizza: {self.name}"


class PizzaFactory(ABC):
    """
    Abstract factory class for creating pizzas.
    """
    @abstractmethod
    def create_pizza(self, name):
        pass


class Margarita(Pizza):
    def __init__(self, name):
        super().__init__(name)


class Pepperoni(Pizza):
    def __init__(self, name):
        super().__init__(name)


class Carbonara(Pizza):
    def __init__(self, name):
        super().__init__(name)


class PizzaFactoryMethod(PizzaFactory):
    """
    Concrete implementation of the PizzaFactory using the Factory Method pattern
    """
    def create_pizza(self, name):
        if name == "Margarita":
            return Margarita(name)
        elif name == "Pepperoni":
            return Pepperoni(name)
        elif name == "Carbonara":
            return Carbonara(name)
        else:
            raise ValueError("Unknown pizza type")


# Testing
factory = PizzaFactoryMethod()

margarita_pizza = factory.create_pizza("Margarita")
pepperoni_pizza = factory.create_pizza("Pepperoni")
carbonara_pizza = factory.create_pizza("Carbonara")

print(margarita_pizza)
print(pepperoni_pizza)
print(carbonara_pizza)
