import threading
'''
Додала обʼєкт блокування з threading.Lock()
метод використовує контекстний менеджер, потік захоплює блокування, і не дає іншим потоком увійти у відповідну секцію
'''


class Director:
    """
    A class that implements singleton of director
    """
    _instance = None
    _lock = threading.Lock()  # added block

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def get_instance(cls, name: str):
        with cls._lock:  # Blocking access to a critical section
            if not cls._instance:
                cls._instance = cls(name)
            return cls._instance

    def make_decision(self, decision) -> None:
        print(f"Director {self.name} makes decision: {decision}")


# test
director1 = Director.get_instance("Test1")
director2 = Director.get_instance("Test2")  # Trying to create a second instance

print(director1 is director2)  # True, same object

director1.make_decision("Make more money")
director2.make_decision("Launch a new product")
