class Subsystem1:
    """
    Subsystem window
    """
    @staticmethod
    def open_window() -> str:
        return "Window opened!"


class Subsystem2:
    """
    Subsystem door
    """

    @staticmethod
    def close_door() -> str:
        return "Door closed!"


class Subsystem3:
    """
    Subsystem wall
    """

    @staticmethod
    def build_wall() -> str:
        return "Wall built!"


class Subsystem4:
    """
    Subsystem lights
    """

    @staticmethod
    def turn_lights() -> str:
        return "Lights turned on!"


class FacadeHouse:
    """
    Facade class
    """

    def __init__(self, window: Subsystem1, door: Subsystem2, wall: Subsystem3, lights: Subsystem4) -> None:
        self._window = window
        self._door = door
        self._wall = wall
        self._lights = lights

    def open_window(self) -> str:
        return self._window.open_window()

    def close_door(self) -> str:
        return self._door.close_door()

    def build_wall(self) -> str:
        return self._wall.build_wall()

    def turn_lights(self) -> str:
        return self._lights.turn_lights()


def client_code(facade: FacadeHouse) -> None:
    """
    Client code
    """
    print(facade.open_window())
    print(facade.close_door())
    print(facade.build_wall())
    print(facade.turn_lights())


# testing

subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
subsystem3 = Subsystem3()
subsystem4 = Subsystem4()
facade_instance = FacadeHouse(subsystem1, subsystem2, subsystem3, subsystem4)
client_code(facade_instance)
