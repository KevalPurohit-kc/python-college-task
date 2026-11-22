class Animal:
    def sound(self):
        print("Animals make different sounds.")


class Dog(Animal):
    def sound(self):
        print("Dog barks.")


class Cat(Animal):
    def sound(self):
        print("Cat meows.")


def make_sound(animal):
    animal.sound()


for animal in (Dog(), Cat()):
    make_sound(animal)