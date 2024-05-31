from abc import ABC, abstractmethod


# Abstraction for TV Control
class TVControlAbstract(ABC):
    def __init__(self, device):
        self._device = device

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    @abstractmethod
    def set_channel(self, channel: int):
        pass


# Concrete implementation of TV
class TVDevice:
    def __init__(self):
        self._is_on = False
        self._channel: int = 0

    def power_on(self):
        self._is_on = True
        print("TV is turned on")

    def power_off(self):
        self._is_on = False
        print("TV is turned off")

    def set_channel(self, channel: int):
        if self._is_on:
            self._channel = channel
            print(f"Channel changed to {channel}")

    def get_channel(self):
        return self._channel


# Abstraction for Remote Control
class RemoteControlAbstract(ABC):
    def __init__(self, device):
        self._device = device

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def change_channel(self, channel: int):
        pass


# Concrete implementation of Remote Control
class BasicRemoteControl(RemoteControlAbstract):
    def turn_on(self):
        self._device.power_on()

    def turn_off(self):
        self._device.power_off()

    def change_channel(self, channel):
        self._device.set_channel(channel)
        print(f"Channel changed to {channel}")


# Creating instances of TV and Remote Control
tv = TVDevice()
remote = BasicRemoteControl(tv)

# Using remote control to operate TV
remote.turn_on()  # Turns on the TV
remote.change_channel(5)  # Changes the channel
remote.turn_off()  # Turns off the TV
