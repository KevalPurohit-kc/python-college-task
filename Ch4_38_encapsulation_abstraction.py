from abc import ABC, abstractmethod


class Account:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


account = Account(1000)
account.show_balance()

square = Square(4)
print("Square area:", square.area())
