from abc import ABC, abstractmethod


class OfficeAbstract(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def quit(self):
        pass

    @abstractmethod
    def take_vacation(self):
        pass


class Employee(OfficeAbstract):
    def __init__(self, name, salary, day_of_vacation):
        self.name: str = name
        self.salary: float = salary
        self.day_vacation: int = day_of_vacation
        self.is_working: bool = True

    def work(self):
        if self.is_working:
            return f"{self.name} is working."
        else:
            return f"{self.name} is not working."

    def quit(self):
        self.is_working = False
        return f"{self.name} has quit the job."

    def take_vacation(self):
        if self.is_working and self.day_vacation > 0:
            self.day_vacation -= 1
            return f"{self.name} is on vacation. Remaining vacation days: {self.day_vacation}"
        elif not self.is_working:
            return f"{self.name} cannot take vacation as they have quit the job."
        else:
            return f"{self.name} cannot take vacation as they have no remaining vacation days."


class CompositeEmployee(OfficeAbstract):
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def work(self):
        result = ""
        for employee in self.employees:
            result += employee.work() + "\n"
        return result

    def quit(self):
        result = ""
        for employee in self.employees:
            result += employee.quit() + "\n"
        return result

    def take_vacation(self):
        result = ""
        for employee in self.employees:
            result += employee.take_vacation() + "\n"
        return result


manager = CompositeEmployee()

john = Employee("John", 50000, 20)
alice = Employee("Alice", 60000, 25)

manager.add_employee(john)
manager.add_employee(alice)

print(manager.work())
print(manager.take_vacation())
print(manager.quit())