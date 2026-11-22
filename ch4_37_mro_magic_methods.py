class First:
    def show(self):
        print("Method from First class")


class Second:
    def show(self):
        print("Method from Second class")


class Child(First, Second):
    pass


obj = Child()
print("Method Resolution Order:", " -> ".join(cls.__name__ for cls in Child.mro()))
obj.show()


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


result = Number(10) + Number(20)
print("Addition using magic methods:", result)
