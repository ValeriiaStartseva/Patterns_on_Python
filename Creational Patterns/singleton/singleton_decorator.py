def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class Director:
    def __init__(self, name):
        self.name = name


# testing
director1 = Director("John")
director2 = Director("Alice")

print(director1 is director2)  
print(director1.name)
print(director2.name)
