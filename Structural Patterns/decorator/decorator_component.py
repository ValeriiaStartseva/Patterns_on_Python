import time


class Component:
    """
    Base Component interface.
    """

    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations.
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
    """
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class StopwatchDecorator(Decorator):
    def operation(self) -> str:
        """
        Decorators for
        """
        start_time = time.time()
        result = self.component.operation()
        end_time = time.time()
        print(f"Time spent: {end_time - start_time} seconds")
        return result


def client_code(component: Component) -> None:
    """
    Func for a client code. Work with component, but independent of the other code
    """

    print(f"RESULT: {component.operation()}", end="")


# testing

# Create an instance of ConcreteComponent
concrete_component = ConcreteComponent()

# Wrap the component with StopwatchDecorator
component_with_stopwatch = StopwatchDecorator(concrete_component)

# Now you can call the operation on each decorated component
component_with_stopwatch.operation()
