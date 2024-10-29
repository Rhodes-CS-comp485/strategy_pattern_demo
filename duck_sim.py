from abc import ABC
from abc import abstractmethod


# The FlightBehavior interface
class FlightBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


# Concrete Strategy 1
class FlightByFlapping(FlightBehavior):
    def fly(self):
        print("I'm flying with wings!")


# Concrete Strategy 2
class FlightByTossing(FlightBehavior):
    def fly(self):
        print("Ah! I'm being tossed in the air!")


# Concrete Strategy 3
class FlightByEngine(FlightBehavior):
    def fly(self):
        print("I'm turbo-speed flying using my engine!")


# The Duck superclass, which uses a FlightBehavior strategy to implement its flying behavior
class Duck(ABC):
    def __init__(self, flight_behavior: FlightBehavior):
        self._flight_behavior = flight_behavior

    def fly(self):
        # delegates flying behavior to the flight_behavior instance
        self._flight_behavior.fly()

    def quack(self):
        print("I'm quacking!")

    @abstractmethod
    def display(self):
        # abstract method that must be implemented by subclasses
        pass


# Specific Duck Subclasses
class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlightByFlapping())

    def display(self):
        print("I'm a Mallard Duck!")


class MandarinDuck(Duck):
    def __init__(self):
        super().__init__(FlightByFlapping())

    def display(self):
        print("I'm a Mandarin Duck!")


class CommonTealDuck(Duck):
    def __init__(self):
        super().__init__(FlightByFlapping())

    def display(self):
        print("I'm a Common Teal Duck!")


class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlightByTossing())

    def quack(self):
        print("I'm squeaking!")

    def display(self):
        print("I'm a Rubber Duck!")


# Client code
if __name__ == "__main__":

    ducks = [
        MallardDuck(),
        MandarinDuck(),
        CommonTealDuck(),
        RubberDuck()
    ]

    for duck in ducks:
        duck.display()
        duck.quack()
        duck.fly()
