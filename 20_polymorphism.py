# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic animal sound"

    def __str__(self):
        return f"{self.name} makes a sound: {self.sound()}"

# Derived class 1
class Dog(Animal):
    def sound(self):
        return "Bark"

# Derived class 2
class Cat(Animal):
    def sound(self):
        return "Meow"

# Derived class 3
class Cow(Animal):
    def sound(self):
        return "Moo"

def main():
    # Create objects of each class
    animals = [
        Dog("Dog"),
        Cat("Cat"),
        Cow("Cow")
    ]
    
    # Demonstrate polymorphism
    for animal in animals:
        print(animal)  # This will call the __str__ method, which in turn calls the overridden sound method

main()
