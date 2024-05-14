import threading


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]


class Director(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name


# Testing
director1 = Director("Test")
director2 = Director("Test2")

print(director1 is director2)
print(director1.name)
print(director2.name)

