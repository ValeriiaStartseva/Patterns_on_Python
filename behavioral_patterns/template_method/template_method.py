from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    Interface for all template methods + algorithm
    """

    def template_method(self) -> None:
        """
        Template method and algorithm
        """

        self.go_to_supermarket()
        self.choice_product()
        self.prepare_products()
        self.make_salad()

    def go_to_supermarket(self) -> None:
        print("AbstractClass says: ")

    def choice_product(self) -> None:
        print("AbstractClass says: ")

    def prepare_products(self) -> None:
        print("AbstractClass says: ")

    def make_salad(self) -> None:
        print("AbstractClass says: ")

    @abstractmethod
    def add_olive_oil(self) -> None:
        pass

    @abstractmethod
    def add_sunflower_oil(self) -> None:
        pass


class MakeGreekSalad(AbstractClass):
    def go_to_supermarket(self) -> None:
        print("Going to the supermarket for Greek Salad ingredients.")

    def choice_product(self) -> None:
        print("Choosing fresh vegetables for Greek Salad.")

    def prepare_products(self) -> None:
        print("Washing and cutting the vegetables for Greek Salad.")

    def make_salad(self) -> None:
        print("Mixing the ingredients to make Greek Salad.")

    def add_olive_oil(self) -> None:
        print("Adding olive oil to Greek Salad.")

    def add_sunflower_oil(self) -> None:
        pass  # Greek Salad does not require sunflower oil


class MakeCesarSalad(AbstractClass):
    def go_to_supermarket(self) -> None:
        print("Going to the supermarket for Caesar Salad ingredients.")

    def choice_product(self) -> None:
        print("Choosing fresh vegetables and chicken for Caesar Salad.")

    def prepare_products(self) -> None:
        print("Washing and cutting the vegetables and chicken for Caesar Salad.")

    def make_salad(self) -> None:
        print("Mixing the ingredients to make Caesar Salad.")

    def add_olive_oil(self) -> None:
        pass  # Caesar Salad does not require olive oil

    def add_sunflower_oil(self) -> None:
        print("Adding sunflower oil to Caesar Salad.")


def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()


# testing
print("Making Greek Salad:")
client_code(MakeGreekSalad())

print("Making Caesar Salad:")
client_code(MakeCesarSalad())