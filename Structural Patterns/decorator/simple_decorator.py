import time


class Decorator:
    def operation(self, func) -> str:
        pass


class StopwatchDecorator(Decorator):
    def operation(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Time spent: {end_time - start_time} seconds")
            return result
        return wrapper

    def __call__(self, func):
        return self.operation(func)

# Example usage:


@StopwatchDecorator()  # Note the parentheses to instantiate the class
def my_function():
    # Your code here
    time.sleep(1)  # Simulating some time-consuming task

my_function()
